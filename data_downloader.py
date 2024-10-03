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

# def filter_short_poems(poems: List[Dict], max_lines: int = 20) -> List[Dict]:
#     """Filter poems to keep only those with at most max_lines lines"""
#     return [poem for poem in poems if len(poem["lines"]) <= max_lines]

def save_to_json(data: Dict, filename: str) -> None:
    """Save the poetry dictionary to a JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    SHORT = True
    try:
        print("Fetching Lord Byron's poems...")
        all_poems = fetch_byron_poems()
        print(f"Found {len(all_poems)} total poems.")
        
        # if SHORT:
        #     short_poems = filter_short_poems(all_poems)
        #     print(f"Found {len(short_poems)} poems with 20 or fewer lines.")
        #     filename = "byron_short_poems.json"
        #     save_to_json(short_poems, filename)
        #     print(f"Successfully saved short poems to {filename}")
        # else:
        filename = "byron_all_poems.json"
        print(f"Successfully saved poems to {filename}")
        save_to_json(all_poems, filename)

        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()