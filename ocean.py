import os
import requests
from dotenv import load_dotenv

load_dotenv()
#Extract the token from the environment
API_KEY = os.getenv("OCEAN_API_KEY")

#this is the url we are going to send request for data

url = "https://api.ocean.io/v3/search/companies"

#header is for authentication + meta data,
#here the api token act as id card to validate whether i am the one who is in need for data
headers = {
    "X-Api-Token": API_KEY,
    "Content-Type": "application/json"
}
#filter to extract country with size of only 5 companies
payload = {
    "size": 5,
    "companiesFilters": {
        "primaryLocations": {
            "includeCountries": ["us"]
        }
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
#since the response in json format we are converting them into the python dictonaries and list
data = response.json()
companies_list = []

for item in data["companies"]:
    company = item["company"]

    print(
        company["name"],
        "-",
        company["domain"],
        "-",
        company["industries"][0]
    )
    companies_list.append({
    "name": company["name"],
    "domain": company["domain"],
    "industry": company["industries"][0]
    })

import pandas as pd

df = pd.DataFrame(companies_list)

print(df)

df.to_csv("companies.csv", index=False)

print("CSV file created successfully")