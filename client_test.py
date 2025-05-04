import requests

res = requests.post(
    "http://127.0.0.1:5000/ask",
    json={"question": "What is machine learning?"}
)

print(res.json())
