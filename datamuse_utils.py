# datamuse_utils.py
import requests

def get_related_keywords(topic: str) -> list:
    
    url = f"https://api.datamuse.com/words?rel_trg={topic}&max=10"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return [item['word'] for item in data]
    else:
        return []  # Return an empty list if the API call fails
