import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(recipient_email, error_update):
    sender_email = os.getenv("sender_email")
    sender_password = os.getenv("sender_password")
    email_template_path = "index.html"

    with open(email_template_path, "r") as template_file:
        email_template = template_file.read()

    email_template = email_template.replace("{bug}", str(error_update))
    subject = "Update " + str(error_update)

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(MIMEText(email_template, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
