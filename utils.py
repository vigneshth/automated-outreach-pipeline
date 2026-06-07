import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Get auth token first
auth_url = "https://api.superflow.run/b2b/createAuthToken/"

payload = {
    "clientId": os.getenv("EAZYREACH_CLIENT_ID"),
    "clientSecret": os.getenv("EAZYREACH_CLIENT_SECRET")
}

auth_response = requests.post(auth_url, json=payload)
auth_token = auth_response.json()["authToken"]

# Check balance
balance_url = "https://api.superflow.run/b2b/getGreenBalance"

headers = {
    "Authorization": f"Bearer {auth_token}"
}

response = requests.get(balance_url, headers=headers)

print("Status:", response.status_code)
print(response.text)