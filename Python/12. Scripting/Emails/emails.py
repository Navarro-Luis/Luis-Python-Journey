import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Luis Navarro'
email['to'] = 'dannynavarro6@gmail.com'
email['subject'] = 'you won a million dollars!!'

email.set_content(html.substitute(name = 'TinTin'),'html')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls #encription mechanism, connect secure to server.
    smtp.login('lnavarro5@fordham.edu','Bambloclat9')
    smtp.send_message(email)
    print('all good boss!')