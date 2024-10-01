import requests
import json
from typing import Dict, List

def fetch_byron_poems() -> List[Dict]:
    """Fetch all poems by Lord Byron from PoetryDB"""
    url = "https://poetrydb.org/author/Lord Byron"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch poems: {response.status_code}")

def save_to_json(data: Dict, filename: str) -> None:
    """Save the poetry dictionary to a JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    try:
        print("Fetching Lord Byron's poems...")
        poems = fetch_byron_poems()
        
        print(f"Found {len(poems)} poems.")
        
        filename = "byron_poems2.json"
        save_to_json(poems, filename)
        print(f"Successfully saved poems to {filename}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()