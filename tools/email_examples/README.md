Email examples (Node & Python)

This folder contains minimal examples for sending email via SMTP and via the SendGrid API.

Node (SMTP - nodemailer)

Install:

npm install nodemailer

Run (set env vars `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `FROM_EMAIL`, `TO_EMAIL`):

node node/smtp_example.js

Node (SendGrid)

Install:

npm install @sendgrid/mail

Run (set env var `SG_API_KEY` or `SENDGRID_API_KEY`):

node node/sendgrid_example.js

Python (SMTP)

Install: (usually already available)

python3 -m pip install --user

Run (set env vars `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `FROM_EMAIL`, `TO_EMAIL`):

python3 python/smtp_example.py

Python (SendGrid)

Install:

python3 -m pip install requests

Run (set `SENDGRID_API_KEY` or `SG_API_KEY`):

python3 python/sendgrid_example.py
