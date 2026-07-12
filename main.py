import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

MAIL_FROM = os.getenv("MAIL_FROM", SMTP_USER)
MAIL_TO = os.getenv("MAIL_TO")


def main():
    if not all([SMTP_SERVER, SMTP_USER, SMTP_PASS, MAIL_TO]):
        raise RuntimeError("Missing SMTP configuration in .env")

    msg = EmailMessage()
    msg["From"] = MAIL_FROM
    msg["To"] = MAIL_TO
    msg["Subject"] = "Sample Message"
    msg.set_content(
        "Hello,\n\n"
        "Lorem ipsum style placeholder email content for testing purposes\n\n"
        "Thank you."
    )

    print(f"Connecting to {SMTP_SERVER}:{SMTP_PORT}...")

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        print("TLS enabled")

        smtp.login(SMTP_USER, SMTP_PASS)
        print("Authenticated")

        smtp.send_message(msg)
        print("Email sent successfully!")


if __name__ == "__main__":
    main()
