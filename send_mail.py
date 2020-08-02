import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()


sender = 'example@gmail.com'
recipient = 'example@gmail.com'

email['Subject'] = 'Enter a subject here'
email.set_content(html.substitute(name='Enter a name: '), 'html')
email['From'] = sender
email['To'] = recipient

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender, 'Enter you password: ')
    for _ in range(150):
        smtp.send_message(email)
    print('Message has been sent succesfully..!!')
