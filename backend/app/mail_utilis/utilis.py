from flask_mail import Mail, Message
from flask import current_app, render_template

mail = Mail(current_app)

def send_email(to, subject, body):
    try:
        msg = Message(
            subject=subject,
            sender=current_app.config['MAIL_DEFAULT_SENDER'],
            recipients=[to],
            body=body
        )
        mail.send(msg)
        print("Email sent successfully.")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

def send_verification_email(email, token):
    base_url = current_app.config['BASE_URL']
    verification_link = f"{base_url}/api/verify-email?token={token}"
    subject = "Verify Your Email"

    body = render_template('email_verification.html', verification_link=verification_link)
    success = send_email(email, subject, body)

    if success:
        print('Email sent successfully')
    else:
        print('Failed to send email')