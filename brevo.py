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

receiver_email = input("Enter receiver email: ")

email = sib_api_v3_sdk.SendSmtpEmail(
    sender={
        "name": "SDE Intern Project",
        "email": SENDER_EMAIL
    },
    to=[
        {
            "email": receiver_email
        }
    ],
    subject="Brevo Test Email",
    html_content="""
    <html>
        <body>
            <h2>Hello Madhu 👋</h2>
            <p>This is a test email sent using Brevo API.</p>
            <p>If you received this email, Brevo is working correctly.</p>
        </body>
    </html>
    """
)

try:
    response = api_instance.send_transac_email(email)
    print("Email sent successfully!")
    print(response)

except ApiException as e:
    print("Error:", e)