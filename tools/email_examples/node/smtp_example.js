const nodemailer = require('nodemailer');

const host = process.env.SMTP_HOST || 'smtp.example.com';
const port = parseInt(process.env.SMTP_PORT || '587', 10);
const user = process.env.SMTP_USER;
const pass = process.env.SMTP_PASS;
const from = process.env.FROM_EMAIL || user;
const to = process.env.TO_EMAIL || 'jimyount1947@gmail.com';

async function send() {
  let transporter = nodemailer.createTransport({
    host,
    port,
    secure: port === 465,
    auth: user && pass ? { user, pass } : undefined,
  });

  const info = await transporter.sendMail({
    from,
    to,
    subject: 'Test email (nodemailer)',
    text: 'Hello from nodemailer example',
  });

  console.log('Message sent:', info.messageId);
}

send().catch((err) => { console.error(err); process.exit(1); });
