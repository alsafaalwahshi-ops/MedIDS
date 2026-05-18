import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_email_alert(subject, message):
    sender = os.getenv("EMAIL_SENDER")
    spass = os.getenv("EMAIL_PASSWORD")
    reciever = os.getenv("EMAIL_RECIEVER")
    
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = reciever
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, spass)
    server.sendmail(sender, reciever, msg.as_string())
    server.quit()
