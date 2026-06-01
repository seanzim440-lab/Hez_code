import os
import smtplib
from email.message import EmailMessage

host = os.environ.get('SMTP_HOST', 'smtp.example.com')
port = int(os.environ.get('SMTP_PORT', 587))
user = os.environ.get('SMTP_USER')
password = os.environ.get('SMTP_PASS')
from_addr = os.environ.get('FROM_EMAIL', user)
to_addr = os.environ.get('TO_EMAIL', 'jimyount1947@gmail.com')

msg = EmailMessage()
msg['Subject'] = 'Test email (smtplib)'
msg['From'] = from_addr
msg['To'] = to_addr
msg.set_content('Hello from smtplib example')

with smtplib.SMTP(host, port) as s:
    if port == 465:
        s = smtplib.SMTP_SSL(host, port)
    else:
        s.ehlo()
        try:
            s.starttls()
        except Exception:
            pass

    if user and password:
        s.login(user, password)
    s.send_message(msg)
    print('Message sent')
