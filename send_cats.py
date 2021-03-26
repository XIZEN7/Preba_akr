import requests
import json
from email.message import EmailMessage
import smtplib

# Api
data = requests.get(
    'https://cat-fact.herokuapp.com/facts/random')
print(data.json()['text'])

# Email Credentials
EMAIL_ADDRESS = 'stevensimpson05@gmail.com'
EMAIL_PASSWORD = 'dpwtsbvdryijofmq'

# Send Email
msg = EmailMessage()
msg['Subject'] = 'Cat Facts'
msg['From'] = EMAIL_ADDRESS
msg['To'] = [EMAIL_ADDRESS, '']
msg.set_content('Hi,' + '\n' + "Have a good day, i'm attaching Cat Facts :)" + '\n'*2 + '-----------------------' +
                '\n' + data.json()['text'])

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
