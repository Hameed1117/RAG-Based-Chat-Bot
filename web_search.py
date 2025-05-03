import requests
import os

SERPER_API_KEY = os.getenv("SERPER_API_KEY", "3debc5fd71d4ed26a31610f554195a59b4576d29")

def search_web(query):
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    data = {"q": query}
    try:
        response = requests.post(url, json=data, headers=headers)
        results = response.json()
        snippets = []

        for item in results.get("organic", [])[:5]:
            snippets.append(f"{item['title']}: {item['snippet']}")
        return "\n".join(snippets)
    except Exception as e:
        return "[ERROR] Web search failed."
