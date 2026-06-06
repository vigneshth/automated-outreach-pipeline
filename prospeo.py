import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PROSPEO_API_KEY")

if not API_KEY:
    raise ValueError("PROSPEO_API_KEY not found in .env")

url = "https://api.prospeo.io/search-person"

headers = {
    "X-KEY": API_KEY,
    "Content-Type": "application/json"
}

all_leads = []

for page in range(1, 6):

    payload = {
        "page": page,
        "filters": {
            "company": {
                "names": {
                    "include": ["OpenAI"]
                }
            }
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    data = response.json()

    if data.get("error"):
        print("Error:", data)
        break

    for result in data.get("results", []):
        person = result["person"]

        all_leads.append({
            "Name": person.get("full_name"),
            "Title": person.get("current_job_title"),
            "LinkedIn": person.get("linkedin_url"),
            "Location": f"{person.get('location', {}).get('city', '')}, {person.get('location', {}).get('state', '')}"
        })

df = pd.DataFrame(all_leads)
df.to_csv("openai_all_leads.csv", index=False)

print(f"Saved {len(df)} leads to openai_all_leads.csv")