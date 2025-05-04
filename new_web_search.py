"""
new_web_search.py
-----------------
Purpose: Provides formatted web search results using Serper.dev API.
          Returns a single string that combines titles and snippets,
          optimized for input into a language model (e.g., in a RAG prompt).
"""


import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def search_web(query):
    if not SERPER_API_KEY:
        return "[ERROR] SERPER_API_KEY is not set in environment."

    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    data = {"q": query}

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        results = response.json()
        snippets = []

        for item in results.get("organic", [])[:5]:
            snippets.append(f"{item['title']}: {item['snippet']}")
        return "\n".join(snippets)

    except Exception as e:
        return f"[ERROR] Web search failed: {str(e)}"
