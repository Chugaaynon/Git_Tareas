#!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
from getpass import getpass


user = "jesus.lazcanomrtn@uanl.edu.mx"
password = getpass()

subjv = "Practica 8 - LPC"

data = {
    "user": user,
    "pass": password,
    "subj": subjv
    }


# create and setup the parameters of the message
email_msg = MIMEMultipart()
email_msg["From"] = data["user"]
receipents = ["elian.hernandezsnch@uanl.edu.mx"]
email_msg["To"] = ", ".join(receipents)
email_msg["Subject"] = data["subj"]

# add in the message body
message = "Hola, mensaje de prueba"
email_msg.attach(MIMEText(message, "plain"))

# create server
server = smtplib.SMTP("smtp.office365.com:587")
server.starttls()
# Login Credentials for sending the mail
server.login(data["user"], data["pass"])


# send the message via the server.
server.sendmail(email_msg["From"], receipents, email_msg.as_string())
server.quit()
print("successfully sent email to %s:" % (email_msg["To"]))
