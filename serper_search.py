"""
serper_search.py
----------------
Purpose: Provides a search function that returns raw snippets (List[str])
          from the Serper.dev API. Useful for evaluation, testing, or
          simple integrations where full formatting is not required.
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SERPER_API_KEY")

def search_serper(query, count=5):
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": API_KEY,
        "Content-Type": "application/json"
    }
    payload = { "q": query }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"[ERROR] Serper API error: {response.status_code} - {response.text}")
        return []

    results = response.json().get("organic", [])
    return [item.get("snippet", "") for item in results[:count] if "snippet" in item]
