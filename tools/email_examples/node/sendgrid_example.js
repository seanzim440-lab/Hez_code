const sg = require('@sendgrid/mail');

if (!process.env.SG_API_KEY && !process.env.SENDGRID_API_KEY) {
  console.error('Set SG_API_KEY or SENDGRID_API_KEY env var');
  process.exit(1);
}

sg.setApiKey(process.env.SG_API_KEY || process.env.SENDGRID_API_KEY);

const from = process.env.FROM_EMAIL || 'no-reply@example.com';
const to = process.env.TO_EMAIL || 'jimyount1947@gmail.com';

async function send() {
  const msg = {
    to,
    from,
    subject: 'Test email (SendGrid @sendgrid/mail)',
    text: 'Hello from SendGrid Node example',
  };

  const res = await sg.send(msg);
  console.log('SendGrid response status:', res[0]?.statusCode);
}

send().catch((err) => { console.error(err); process.exit(1); });
