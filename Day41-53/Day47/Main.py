import smtplib
from os import environ
import dotenv

import bs4 as bs
import requests
from dotenv import load_dotenv

URL="https://appbrewery.github.io/instant_pot/"

#FROM_ADDRESS = 'study.creekworm@gmail.com'
#APP_USERNAME='PythonApp'
#APP_PASSWORD = 'jgaa evmn nxwz osez'
load_dotenv(verbose=True)
def send_email(subject,body, to):
    APP_USERNAME = environ.get("APP_USERNAME")
    APP_PASSWORD = environ.get("APP_PASSWORD")
    FROM_ADDRESS = environ.get("FROM_ADDRESS")

    with smtplib.SMTP('smtp.gmail.com', 25) as smtp_client:
        print(f'Sending email. to: {to}')
        smtp_client.starttls()
        login = smtp_client.login(FROM_ADDRESS, APP_PASSWORD)
        message=f"SUBJECT:{subject}\n\n{body}"
        smtp_client.sendmail(FROM_ADDRESS,to,message)

send_email("price reduced","sa","manas.nayak@outlook.com")
response = requests.get(URL).text
soup = bs.BeautifulSoup(response, "html.parser")

prod_price_div = soup.find("div", {"data-csa-c-slot-id": "corePriceDisplay_desktop_feature_div"})
price=float(prod_price_div.select_one("span.aok-offscreen").text.split("$")[1])
print(price)

