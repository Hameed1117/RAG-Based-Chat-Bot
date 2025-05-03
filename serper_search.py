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
