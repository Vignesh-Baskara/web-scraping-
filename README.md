# Event Scraper with Email Notifications

A Python script that scrapes event information from a website, stores new events in a file, and sends email notifications for new events. The script continuously checks for updates, ensuring you never miss a new event.

## Features

- **Web Scraping**: Fetches event data from a specified URL.
- **Data Storage**: Stores unique events in a local text file (`data.txt`).
- **Email Notifications**: Sends email alerts when new events are found.
- **Automation**: Continuously monitors the website for updates.
## Prerequisites

1. Python 3.x installed on your system.
2. Required Python libraries:
   - `requests`
   - `selectorlib`
   - `smtplib`
   - `sqlite3`
   - `ssl`
3. An SMTP email account for sending notifications.

## Installation. 

git clone https://github.com/yourusername/event-scraper.git
   cd event-scraper

### pip install requests selectorlib

#### Usage
Set Up Email Credentials:

Use an environment variable to securely store your email password:
bash
Copy code
export PASSKEY='your_email_password'
Replace 'your_email_password' with the actual password for the email account.

Prepare the Selector File:

Ensure extract.yaml is in the same directory. This file should define the selectors for scraping event data.
Run the Script:

bash
Copy code
python your_script_name.py
File Structure
data.txt: Stores previously detected events to avoid duplication.
extract.yaml: Contains the CSS selectors for scraping data.
data.db: SQLite database connection for potential future extensions.
How It Works
The script scrapes the target website for event data.
Extracts relevant details using the extract.yaml file.
Compares the extracted data with existing records in data.txt.
If a new event is found:
It is stored in data.txt.
An email notification is sent to the configured recipient.
Example Output
Console:

plaintext
Copy code
New event found: 'Tigers in Tiger City on 2088.10.14'
Data stored successfully.
Email was sent.
Email Notification:

vbnet
Copy code
Subject: New Event Alert
Body: Hey, a new event was found: Tigers in Tiger City on 2088.10.14.
Future Enhancements
Add database integration for improved data management.
Support multiple email recipients.
Implement a web interface for monitoring.
### License
This project is open-source and available under the MIT License.

# Author
## Vignesh BAskar

### Steps to Follow
1. Replace placeholders like `your_script_name.py`, `yourusername`, and `your_email_password` with actual details.
2. Ensure your `extract.yaml` file is correctly set up for scraping.
3. Customize the "Future Enhancements" and "Author" sections as needed.

Let me know if you need further assistance!

