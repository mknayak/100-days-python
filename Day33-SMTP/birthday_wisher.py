import datetime as dt
import smtplib
import random
import pandas as pd

FROM_ADDRESS = 'study.creekworm@gmail.com'
APP_USERNAME='PythonApp'
APP_PASSWORD = 'jgaa evmn nxwz osez'

def send_email(subject,body, to):
    with smtplib.SMTP('smtp.gmail.com', 25) as smtp_client:
        print(f'Sending email. to: {to}')
        smtp_client.starttls()
        login = smtp_client.login(FROM_ADDRESS, APP_PASSWORD)
        message=f"SUBJECT:{subject}\n\n{body}"
        smtp_client.sendmail(FROM_ADDRESS,to,message)

birthdays = pd.read_csv('birthdays.csv')
now = dt.datetime.now()
month = now.month
day = now.day
# print(birthdays)

filtered_birthdays = birthdays[(birthdays['month']==month) & (birthdays['day']==day)]
# print(filtered_birthdays)
# print(type(filtered_birthdays))

if not filtered_birthdays.empty:
    for bd in filtered_birthdays.to_dict(orient='records'):
        to_email=bd['email']
        name=bd["name"]
        letter_int = random.randint(1,3)
        with open(f"./letter_templates/letter_{letter_int}.txt","r") as file:
            content = file.read()
        e_subject= f"Happy Birthday!!"
        e_body= content.replace("[NAME]", name)
        send_email(e_subject,e_body,to_email)
