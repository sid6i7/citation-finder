import requests
import logging
from model.config import *
from model.preprocess import PreProcessor
from sentence_transformers import SentenceTransformer, util

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
    ]
)

logger = logging.getLogger(__name__)

class DataHandler:
    """
    A class to handle fetching of data from an external endpoint.
    """

    def __init__(self) -> None:
        """
        Initializes the DataHandler instance and fetches messages data.
        """
        self.data = self.__fetch_messages()

    def __fetch_messages(self):
        """
        Fetches messages from a predefined endpoint.

        Returns:
            dict: The JSON response containing messages data.
        """
        logging.info("Fetching messages")
        messages_data = None
        try:
            response = requests.get(
                GET_MESSAGES_ENDPOINT,
                headers=HEADERS
            )
            response.raise_for_status()
            messages_data = response.json()
        except Exception as e:
            logging.error(f"Some error occured {e}")
        return messages_data


class Model:
    """
    A class to handle the processing of responses and sources, and to calculate
    the similarities between them using SentenceTransformer embeddings.
    """

    def __init__(self, rawData) -> None:
        """
        Initializes the Model instance, processes the data, and encodes the text
        using the SentenceTransformer model.
        """
        logging.info("initializing model")
        self.preprocessor = PreProcessor(rawData)
        self.responses, self.sources = self.preprocessor.preprocess()
        self.model = SentenceTransformer('distilbert-base-nli-mean-tokens')
        self.__get_sentence_embeddings()
    
    def __get_sentence_embeddings(self):
        """
        Encodes the responses and sources using the SentenceTransformer model.
        """
        logging.info("start generating sentence embeddings")
        for idx, response in enumerate(self.responses):
            embedded_response = self.model.encode(response['text'])
            self.responses[idx]['embeddings'] = embedded_response
        for i, sources in enumerate(self.sources):
            for j, source in enumerate(sources):
                embedded_source = self.model.encode(source['context'])
                self.sources[i][j]['embeddings'] = embedded_source
        logging.info("finish generating sentence embeddings")
    
    def get_citations(self):
        """
        Calculate similarities between responses and their sources using SentenceTransformer embeddings,
        and assign citations to each response based on a predefined similarity threshold.

        Returns:
            list: The updated list of responses with citations.
        """
        logging.info("start finding citations")
        for idx, response in enumerate(self.responses):
            response_embedding = response['embeddings']
            citations = []

            for source in self.sources[idx]:
                source_embedding = source['embeddings']
                similarity = util.pytorch_cos_sim(response_embedding, source_embedding).item()
                if similarity > SIMILARITY_THRESHOLD:
                    citations.append({
                        'id': source['id'],
                        'link': source['link']
                    })

            self.responses[idx]['citations'] = citations
            del self.responses[idx]['embeddings']
        logging.info("finish finding citations")
        return self.responses