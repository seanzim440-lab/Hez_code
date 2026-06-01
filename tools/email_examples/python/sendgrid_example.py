import os
import requests
import json

API_KEY = os.environ.get('SENDGRID_API_KEY') or os.environ.get('SG_API_KEY')
if not API_KEY:
    raise SystemExit('Set SENDGRID_API_KEY or SG_API_KEY environment variable')

from_addr = os.environ.get('FROM_EMAIL', 'no-reply@example.com')
to_addr = os.environ.get('TO_EMAIL', 'jimyount1947@gmail.com')

url = 'https://api.sendgrid.com/v3/mail/send'
payload = {
  "personalizations": [{"to":[{"email": to_addr}], "subject":"Test email (SendGrid API)"}],
  "from": {"email": from_addr},
  "content":[{"type":"text/plain","value":"Hello from SendGrid API (Python)"}]
}
headers = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}

r = requests.post(url, headers=headers, data=json.dumps(payload))
print(r.status_code, r.text)
