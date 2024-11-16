import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3
import time

"INSERT INTO events VALUES ('Tigers', 'Tiger City', '2088.10.14')"
"SELECT * FROM events WHERE date='2088.10.15'"

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect("data.db")

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "vickyasvickyb@gmail.com"
    password = os.getenv('PASSKEY')

    receiver = "vickyasvickyb@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    print("Email was sent")




def store(extracted):
    """Store extracted data in a text file with error handling"""
    try:
        with open("data.txt", 'a') as file:
            file.write(extracted + "\n")
        print("Data stored successfully.")
    except Exception as e:
        print(f"Error while storing data: {e}")


def read(extracted):
    with open ("data.txt", 'r') as file:
        return file.read()



if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        content = read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                print("extracted value stored successfully")
                send_mail(message = "Hey new event was found ")

        time.sleep(2)