# Automated Outreach Pipeline

## Overview

Automated Outreach Pipeline is a Python-based project that automates the process of finding potential business leads from a target company domain.

The pipeline performs the following tasks:

1. Accepts a company domain as input.
2. Finds similar companies using Ocean.io.
3. Extracts decision-makers and key contacts using Prospeo.
4. Stores lead information in CSV format.
5. Optionally sends personalized outreach emails using Brevo.

This project demonstrates API integration, data processing, automation workflows, and lead generation techniques.

---

## Features

* Company discovery using Ocean.io
* Lead generation using Prospeo
* CSV export of collected leads
* Automated email outreach using Brevo
* Modular and reusable Python code
* Environment variable support using dotenv

---

## Technologies Used

* Python 3
* Ocean.io API
* Prospeo API
* Brevo Email API
* Pandas
* Requests
* Python Dotenv

---

## Project Structure

```text
automated-outreach-pipeline/
│
├── main.py
├── ocean.py
├── prospeo.py
├── brevo.py
├── requirements.txt
├── companies.csv
├── all_leads.csv
├── .env
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/vigneshth/automated-outreach-pipeline.git
cd automated-outreach-pipeline
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
OCEAN_API_KEY=your_ocean_api_key
PROSPEO_API_KEY=your_prospeo_api_key
BREVO_API_KEY=your_brevo_api_key
SENDER_EMAIL=your_email@example.com
```

---

## Running the Project

```bash
python main.py
```

Example:

```text
Enter company domain: leadsquared.com
```

---

## Workflow

### Stage 1 – Company Discovery

Finds companies similar to the provided domain using Ocean.io.

### Stage 2 – Lead Generation

Searches Prospeo for decision-makers such as:

* CEO
* CTO
* Director
* VP
* Founder

### Stage 3 – Email Outreach

Sends personalized outreach emails using Brevo.

---

## Sample Output

```text
Companies Found : 5
Contacts Found  : 6

Send Emails? (Y/N): N

Pipeline Finished.
```

---

## Generated Files

### companies.csv

Contains discovered companies.

### all_leads.csv

Contains generated leads and contact details.

---

## Learning Outcomes

Through this project I learned:

* API integration
* Lead generation workflows
* Data extraction and processing
* CSV automation
* Email automation
* Python project structuring
* Environment variable management

---

## Author

Madhu Vignesh

GitHub:
https://github.com/vigneshth

```
```
