import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from config import *

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

class PreProcessor:
    """
    A class to handle preprocessing of raw text data, including cleaning and lemmatization.
    """

    def __init__(self, rawData) -> None:
        """
        Initializes the PreProcessor instance.

        Args:
            rawData (dict): The raw data to be preprocessed.
        """
        self.stopWords = stopwords.words('english')
        self.lemmatizer = WordNetLemmatizer()
        self.rawData = rawData

    def preprocess(self):
        """
        Preprocesses the raw data by parsing and cleaning the text.

        Returns:
            tuple: Two lists containing cleaned responses and sources.
        """
        responses, sources = self.__parse_data(self.rawData)
        clean_responses, clean_sources = self.__preprocess_text(responses, sources)
        return clean_responses, clean_sources
    
    def __parse_data(self, rawData):
        """
        Parses the raw data to extract responses and their sources.

        Args:
            rawData (dict): The raw data to be parsed.

        Returns:
            tuple: Two lists containing responses and sources.
        """
        all_responses = []
        all_sources = []
        if rawData['data']['data']:
            data = rawData['data']['data']
            for group in data:
                all_responses.append({
                    'id': group['id'],
                    'text': group['response']
                })
                if group['source']:
                    all_sources.append(group['source'])
        return all_responses, all_sources
    
    def __preprocess_text(self, responses, sources):
        """
        Cleans the text of responses and sources.

        Args:
            responses (list): The list of responses to be cleaned.
            sources (list): The list of sources to be cleaned.

        Returns:
            tuple: Two lists containing cleaned responses and sources.
        """
        for idx, response in enumerate(responses):
            clean_text = self.clean_text(response['text'])
            responses[idx]['text'] = clean_text
        for i, currSources in enumerate(sources):
            for j, source in enumerate(currSources):
                if 'context' in source:
                    clean_context = self.clean_text(source['context'])
                    sources[i][j]['context'] = clean_context
        return responses, sources
        
    def clean_text(self, text):
        """
        Cleans a given text by removing URLs, HTML tags, punctuation, and stopwords,
        and performing lemmatization.

        Args:
            text (str): The input text to be cleaned.

        Returns:
            str: The cleaned text.
        """
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        text = re.sub(r'<.*?>', '', text)
        text = text.translate(str.maketrans('', '', string.punctuation))
        text is text.lower()
        words = word_tokenize(text)
        cleanWords = []
        for word in words:
            if word not in self.stopWords:
                cleanWords.append(self.lemmatizer.lemmatize(word))
        
        return " ".join(cleanWords)