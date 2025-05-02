
import requests

url = 'https://bolls.life/get-verses/'
headers = {
    "Content-Type": "application/json"
}

def bolls_life_client(data):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        print(result)

        return result
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
