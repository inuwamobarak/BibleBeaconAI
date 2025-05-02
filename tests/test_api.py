import requests

url = 'https://bolls.life/get-verses/'

data = [
    {
        "translation": "YLT",
        "book": 19,
        "chapter": 145,
        "verses": [14, 15, 16]
    },
    {
        "translation": "KJV",
        "book": 19,
        "chapter": 91,
        "verses": [1, 2, 3]
    }
]

headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    result = response.json()
    print(result)  # Pretty-print or process as needed
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
