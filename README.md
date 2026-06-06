# Automated Outreach Pipeline

## Overview

This project automates the complete B2B outreach workflow using multiple APIs.

A user provides a single company domain as input. The pipeline then:

1. Finds similar companies using Ocean.io
2. Finds decision-makers using Prospeo
3. Resolves work emails using EazyReach
4. Sends personalized outreach emails using Brevo

The goal is to create a fully automated outreach engine with minimal human intervention.

---

## Pipeline Flow

Seed Domain
↓
Ocean.io
↓
Similar Companies
↓
Prospeo
↓
Decision Makers + LinkedIn URLs
↓
EazyReach
↓
Verified Work Emails
↓
Brevo
↓
Personalized Outreach Emails

---

## Technologies Used

* Python
* Ocean.io API
* Prospeo API
* EazyReach API
* Brevo API
* Pandas
* Requests
* Python Dotenv

---

## Project Structure

automated-outreach-pipeline/

├── ocean.py

├── prospeo.py

├── brevo.py

├── main.py (to be integrated)

├── requirements.txt

├── .gitignore

└── README.md

---

## Stage 1 – Ocean.io

Input:

Company Domain

Example:

openai.com

Output:

companies.csv

Features:

* Ocean.io API integration
* Similar company discovery
* CSV export
* Error handling

---

## Stage 2 – Prospeo

Input:

companies.csv

Output:

all_leads.csv

Features:

* Decision-maker extraction
* CEO / CTO / VP filtering
* LinkedIn URL collection
* Rate-limit handling
* CSV export

---

## Stage 3 – EazyReach

Input:

LinkedIn URLs

Output:

Verified work emails

Features:

* Email enrichment
* Email verification
* CSV export

Status:

Pending API credits

---

## Stage 4 – Brevo

Input:

Verified work emails

Output:

Personalized outreach emails

Features:

* Brevo API integration
* Verified sender setup
* Automated email sending
* Delivery confirmation

---

## Environment Variables

Create a .env file:

OCEAN_API_KEY=your_ocean_api_key

PROSPEO_API_KEY=your_prospeo_api_key

EAZYREACH_API_KEY=your_eazyreach_api_key

BREVO_API_KEY=your_brevo_api_key

SENDER_EMAIL=your_verified_sender_email

---

## Installation

Install dependencies:

pip install -r requirements.txt

---

## Running the Project

Current Modules:

python ocean.py

python prospeo.py

python brevo.py

Future End-to-End Execution:

python main.py

---

## Error Handling

The pipeline handles:

* Missing API keys
* Missing data fields
* API rate limits
* No search results
* Partial failures
* Duplicate contacts

---

## Future Improvements

* Complete EazyReach integration
* Build unified main.py pipeline
* Add safety checkpoint before sending emails
* Add logging system
* Add retry mechanism for failed API requests

---

## Author

Madhu Vignesh

SDE Intern Assignment Project
