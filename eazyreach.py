import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("EAZYREACH_CLIENT_ID")
CLIENT_SECRET = os.getenv("EAZYREACH_CLIENT_SECRET")


def get_auth_token():

    url = "https://api.superflow.run/b2b/createAuthToken/"

    payload = {
        "clientId": CLIENT_ID,
        "clientSecret": CLIENT_SECRET
    }

    response = requests.post(
        url,
        json=payload
    )

    if response.status_code != 200:

        print("Authentication Failed")
        print(response.text)

        return None

    return response.json()["authToken"]


def get_emails(leads):

    auth_token = get_auth_token()

    if not auth_token:
        return []

    contacts = []

    url = "https://api.superflow.run/b2b/linkedin-emails"

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    for lead in leads:

        linkedin_url = lead["LinkedIn"]

        print(
            f"Searching email for {linkedin_url}"
        )

        payload = {
            "linkedinUrl": linkedin_url
        }

        try:

            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=60
            )

            data = response.json()

            print(data)

            if data.get(
                "message"
            ) == "Zero Balance please recharge.":

                print(
                    "\nEazyReach credits exhausted"
                )

                break

            contacts.append({
                "name": lead["Name"],
                "company": lead["Company"],
                "linkedin": linkedin_url,
                "email_data": data
            })

        except Exception as e:

            print("Error:", e)

    df = pd.DataFrame(contacts)

    df.to_csv(
        "verified_emails.csv",
        index=False
    )

    print(
        "\nverified_emails.csv created successfully"
    )

    return contacts


if __name__ == "__main__":

    leads_df = pd.read_csv(
        "all_leads.csv"
    )

    leads = leads_df.to_dict(
        orient="records"
    )

    contacts = get_emails(
        leads
    )

    print(
        f"\nTotal Records: {len(contacts)}"
    )