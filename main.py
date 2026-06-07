from ocean import get_companies
from prospeo import get_leads
from brevo import send_emails


def main():

    print("\n==============================")
    print("AUTOMATED OUTREACH PIPELINE")
    print("==============================")

    domain = input(
        "\nEnter company domain: "
    ).strip()

    # Stage 1 - Ocean.io
    companies = get_companies(
        domain
    )

    if not companies:

        print(
            "\nNo companies found."
        )

        return

    # Stage 2 - Prospeo
    contacts = get_leads(
        companies
    )

    if not contacts:

        print(
            "\nNo contacts found."
        )

        return

    # Pipeline Summary
    print("\n====================")
    print("PIPELINE SUMMARY")
    print("====================")

    print(
        f"Companies Found : {len(companies)}"
    )

    print(
        f"Contacts Found  : {len(contacts)}"
    )

    # Safety Checkpoint
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