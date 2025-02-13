import datetime as dt
import smtplib
import random
FROM_ADDRESS = 'study.creekworm@gmail.com'
APP_USERNAME='PythonApp'
APP_PASSWORD = 'jgaa evmn nxwz osez'

def send_email(subject,body, to):
    with smtplib.SMTP('smtp.gmail.com', 25) as smtp_client:
        smtp_client.starttls()
        login = smtp_client.login(FROM_ADDRESS, APP_PASSWORD)
        message=f"SUBJECT:{subject}\n\n{body}"
        smtp_client.sendmail(FROM_ADDRESS,to,message)

day_of_week=dt.datetime.today().weekday()
if day_of_week==0: #0:Monday - 7: Sunday
    with open("quotes.txt") as file:
        lines = file.readlines()

    r_line= random.choice(lines).strip()
    send_email("Monday Wishes",r_line,"manas.nayak@outlook.com")
