from ocean import get_companies
from prospeo import get_leads
from eazyreach import get_emails
from brevo import send_emails


def main():

    print("\n==============================")
    print("AUTOMATED OUTREACH PIPELINE")
    print("==============================")

    domain = input(
        "\nEnter company domain: "
    ).strip()

    # Stage 1
    companies = get_companies(domain)

    if not companies:
        print("\nNo companies found.")
        return

    # Stage 2
    leads = get_leads(companies)

    if not leads:
        print("\nNo leads found.")
        return

    # Stage 3
    contacts = get_emails(leads)

    print("\n====================")
    print("PIPELINE SUMMARY")
    print("====================")

    print(
        f"Companies Found : {len(companies)}"
    )

    print(
        f"Leads Found     : {len(leads)}"
    )

    print(
        f"Emails Found    : {len(contacts)}"
    )

    choice = input(
        "\nSend Emails? (Y/N): "
    )

    if choice.upper() == "Y":

        send_emails(
            contacts
        )

    else:

        print(
            "\nEmail sending cancelled."
        )

    print(
        "\nPipeline Finished."
    )


if __name__ == "__main__":
    main()