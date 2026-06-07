import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PROSPEO_API_KEY")

if not API_KEY:
    raise ValueError("PROSPEO_API_KEY not found in .env")


def get_leads(companies):

    url = "https://api.prospeo.io/search-person"

    headers = {
        "X-KEY": API_KEY,
        "Content-Type": "application/json"
    }

    print(f"\nSearching {len(companies)} companies...\n")

    all_leads = []

    for company in companies:

        company_name = company["name"]
        company_domain = company["domain"]

        print(f"\nSearching leads for {company_name}")

        payload = {
            "page": 1,
            "filters": {
                "company": {
                    "websites": {
                        "include": [company_domain]
                    }
                },
                "person_seniority": {
                    "include": [
                        "C-Suite",
                        "Vice President",
                        "Director"
                    ]
                }
            }
        }

        try:

            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=30
            )

            print(
                f"{company_name} | Status: {response.status_code}"
            )

            data = response.json()
            print("\nResponse Body:")
            print(data)

            if response.status_code == 429:
                print(
                    "Rate limit exceeded. Waiting 10 seconds..."
                )
                time.sleep(10)
                continue

            if data.get("error_code") == "NO_RESULTS":
                print("No contacts found")
                continue

            if data.get("error"):
                print("Error:", data)
                continue

            results = data.get("results", [])

            for result in results:

                person = result.get("person", {})

                print(
                    person.get("full_name"),
                    "-",
                    person.get("current_job_title")
                )

                all_leads.append({
                    "Company": company_name,
                    "Domain": company_domain,
                    "Name": person.get("full_name"),
                    "Title": person.get("current_job_title"),
                    "LinkedIn": person.get("linkedin_url"),
                    "Location":
                        f"{person.get('location', {}).get('city', '')}, "
                        f"{person.get('location', {}).get('state', '')}"
                })
            time.sleep(2)

        except Exception as e:

            print("Error:", e)

    df = pd.DataFrame(all_leads)

    if not df.empty:

        df.drop_duplicates(
            subset=["LinkedIn"],
            inplace=True
        )

    df.to_csv(
        "all_leads.csv",
        index=False
    )

    print("\n==============================")
    print(f"Saved {len(df)} leads")
    print("Output file: all_leads.csv")
    print("==============================")

    return all_leads


if __name__ == "__main__":

    companies_df = pd.read_csv(
        "companies.csv"
    )

    companies = companies_df.to_dict(
        orient="records"
    )

    leads = get_leads(
        companies
    )

    print(
        f"\nTotal Leads Found: {len(leads)}"
    )



"""

FLOW OF THE CODE 

companies.csv
      ↓
Read one company
      ↓
Call Prospeo API
      ↓
Get employees
      ↓
Filter decision-makers
      ↓
Store leads
      ↓
all_leads.csv


┌─────────────────────┐
│ Start Program       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Load .env file      │
│ Get PROSPEO_API_KEY │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Read companies.csv  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ For each company    │
│ in companies.csv    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Extract             │
│ company_name        │
│ company_domain      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Create Prospeo      │
│ API Payload         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Send POST Request   │
│ to Prospeo API      │
└──────────┬──────────┘
           │
           ▼
      ┌───────────┐
      │ Status?   │
      └─────┬─────┘
            │
 ┌──────────┼──────────┐
 │          │          │
 ▼          ▼          ▼

429      NO_RESULTS   200
 │           │         │
 ▼           ▼         ▼

Wait 10s   Skip      Get JSON
Continue   Company   Response
                       │
                       ▼
            ┌──────────────────┐
            │ Extract results  │
            │ list             │
            └────────┬─────────┘
                     │
                     ▼
            ┌──────────────────┐
            │ For each person  │
            │ in results       │
            └────────┬─────────┘
                     │
                     ▼
            ┌──────────────────┐
            │ Get Job Title    │
            └────────┬─────────┘
                     │
                     ▼
            ┌──────────────────┐
            │ Decision Maker?  │
            │ CEO/CTO/CFO/etc  │
            └───────┬──────────┘
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼

        NO                  YES
          │                   │
          ▼                   ▼

       Skip            Save Lead
                        to list
                            │
                            ▼
                 ┌─────────────────┐
                 │ Store Company   │
                 │ Name            │
                 │ Domain          │
                 │ Person Name     │
                 │ Title           │
                 │ LinkedIn URL    │
                 │ Location        │
                 └────────┬────────┘
                          │
                          ▼
                 Next Person
                          │
                          ▼
                 Next Company
                          │
                          ▼
┌──────────────────────────────┐
│ Convert all_leads to DataFrame│
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Remove Duplicate LinkedIn    │
│ Profiles                     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Save as all_leads.csv        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Print Total Leads Saved      │
└──────────────┬───────────────┘
               │
               ▼
         End Program

"""