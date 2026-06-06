import os
import requests
from dotenv import load_dotenv

load_dotenv()
#Extract the token from the environment
API_KEY = os.getenv("OCEAN_API_KEY")

if not API_KEY:
    raise ValueError("OCEAN_API_KEY not found in .env")

#this is the url we are going to send request for data

url = "https://api.ocean.io/v3/search/companies"

#header is for authentication + meta data,
#here the api token act as id card to validate whether i am the one who is in need for data
headers = {
    "X-Api-Token": API_KEY,
    "Content-Type": "application/json"
}
#filter to extract
seed_domain = input("Enter company domain: ")

payload = {
    "size": 5,
    "companiesFilters": {
        "lookalikeDomains": [
            seed_domain
        ]
    }
}
#storing that in the response object
response = requests.post(
    url,
    headers=headers,
    json=payload
)
#status 
print("Status:", response.status_code)

if response.status_code != 200:
    print("API Error:", response.text)
    exit()

#since the response in json format we are converting them into the python dictonaries and list
data = response.json()
companies_list = []

for item in data["companies"]:
    company = item["company"]

    industry = (
        company["industries"][0]
        if company.get("industries")
        else "Unknown"
    )

    print(
        company["name"],
        "-",
        company["domain"],
        "-",
        industry
    )

    companies_list.append({
        "name": company["name"],
        "domain": company["domain"],
        "industry": industry
    })

import pandas as pd

df = pd.DataFrame(companies_list)

print(df)

df.to_csv("companies.csv", index=False)

print("CSV file created successfully")



"""
┌─────────────────────┐
│ Start Program       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Load .env file      │
│ Get OCEAN_API_KEY   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Ask User for        │
│ Seed Domain         │
│ (e.g. openai.com)   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Create API Payload  │
│ with Seed Domain    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Send POST Request   │
│ to Ocean.io API     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Receive Response    │
│ from Ocean.io       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Convert JSON        │
│ Response to Python  │
│ Dictionary          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Create Empty List   │
│ companies_list      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ For Each Company    │
│ in Response         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Extract             │
│ Company Name        │
│ Domain              │
│ Industry            │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Print Company       │
│ Details             │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Add Company Data    │
│ to companies_list   │
└──────────┬──────────┘
           │
           ▼
      More Companies?
           │
      Yes ─┘
           │
           ▼
┌─────────────────────┐
│ Convert List to     │
│ Pandas DataFrame    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Save DataFrame as   │
│ companies.csv       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Print Success       │
│ Message             │
└──────────┬──────────┘
           │
           ▼
        End Program
"""