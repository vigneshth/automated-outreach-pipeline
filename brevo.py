import os
from dotenv import load_dotenv
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

configuration = sib_api_v3_sdk.Configuration()

configuration.api_key["api-key"] = BREVO_API_KEY

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
    sib_api_v3_sdk.ApiClient(configuration)
)


def send_emails(contacts):

    if not contacts:

        print("No contacts available")

        return 0

    sent_count = 0

    for contact in contacts:

        name = contact.get("Name")
        company = contact.get("Company")
        receiver_email = contact.get("Email")

        if not receiver_email:

            print(
                f"Skipping {name} - email not found"
            )

            continue

        email = sib_api_v3_sdk.SendSmtpEmail(

            sender={
                "name": "Madhu Vignesh",
                "email": SENDER_EMAIL
            },

            to=[
                {
                    "email": receiver_email
                }
            ],

            subject=f"Partnership Opportunity for {company}",

            html_content=f"""
            <html>
                <body>

                    <h2>Hello {name} 👋</h2>

                    <p>
                        I came across {company}
                        and wanted to explore a potential
                        partnership opportunity.
                    </p>

                    <p>
                        We are working on outreach automation
                        solutions that help teams identify
                        prospects, enrich contact information,
                        and automate personalized communication.
                    </p>

                    <p>
                        I would love to connect and discuss
                        whether there may be opportunities
                        to collaborate.
                    </p>

                    <p>
                        Looking forward to hearing from you.
                    </p>

                    <br>

                    <p>
                        Regards,<br>
                        Madhu Vignesh
                    </p>

                </body>
            </html>
            """
        )

        try:

            api_instance.send_transac_email(
                email
            )

            print(
                f"Email sent to {receiver_email}"
            )

            sent_count += 1

        except ApiException as e:

            print(
                f"Failed to send email to {receiver_email}"
            )

            print("Error:", e)

    print("\n==============================")
    print(f"Total Emails Sent: {sent_count}")
    print("==============================")

    return sent_count


if __name__ == "__main__":

    contacts = [
        {
            "Name": "Test User",
            "Company": "Test Company",
            "Email": "test@example.com"
        }
    ]

    send_emails(
        contacts
    )