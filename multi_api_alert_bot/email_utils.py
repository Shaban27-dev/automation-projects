from email.message import EmailMessage
import smtplib
from config import EMAIL, PASSWORD, RECIPIENT
from utils import log_error


def send_email(subject, body):
    try:
        if not EMAIL or not PASSWORD:
            raise ValueError("Email credentials missing")

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL
        msg["To"] = RECIPIENT
        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(EMAIL, PASSWORD)
            connection.send_message(msg)

        print("📧 Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("❌ Email login failed. Check credentials.")
    except smtplib.SMTPException as e:
        log_error(e)
        print(f"❌ SMTP error: {e}")
    except Exception as e:
        log_error(e)
        print(f"❌ Unexpected email error: {e}")