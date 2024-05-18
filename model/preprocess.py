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

    def __init__(self, rawData) -> None:
        self.stopWords = stopwords.words('english')
        self.lemmatizer = WordNetLemmatizer()
        self.data = self.__parse_data(rawData)
    
    def __parse_data(self, rawData):
        pass

    def clean_text(self, text):
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        text = re.sub(r'<.*?>', '', text)
        text = text.translate(str.maketrans('', '', string.punctuation))

        text = text.lower()
        words = word_tokenize(text)
        cleanWords = []
        for word in words:
            if word not in self.stopWords:
                cleanWords.append(self.lemmatizer.lemmatize(word))
        
        return cleanWords
        

