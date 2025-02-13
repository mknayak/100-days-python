import smtplib
FROM_ADDRESS = 'study.creekworm@gmail.com'
APP_USERNAME='PythonApp'
APP_PASSWORD = 'jgaa evmn nxwz osez'

# with smtplib.SMTP('smtp.gmail.com', 25) as smtp_client:
#     smtp_client.starttls()
#     login = smtp_client.login(FROM_ADDRESS, APP_PASSWORD)
#     subject="Hello User"
#     body="Welcome to Python Programming"
#
#     message=f"SUBJECT:{subject}\n\n{body}"
#     smtp_client.sendmail(FROM_ADDRESS,'manas.nayak@outlook.com',message)


# import datetime as dt
#
# now=dt.datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.weekday())