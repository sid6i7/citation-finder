import requests
from config import *

class Model:
    
    def fetch_messages(self):
        messages_data = None
        try:
            response = requests.get(
                GET_MESSAGES_ENDPOINT,
                headers=HEADERS
            )
            response.raise_for_status()
            messages_data = response.json()
        except Exception as e:
            print(f"Some error occured {e}")
        return messages_data