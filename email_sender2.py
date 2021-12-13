import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("html.html").read_text())



email = EmailMessage()

email["from"] = "prathamesh nirmal"
email["to"] = "nirmalprathmesh35@gmail.com"
email["subject"] = "you won 10000$"

email.set_content(html.substitute(name="prathamesh"), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("nirmalprathamesh46gmail.com", "$prat3546$")
    smtp.send_message(email)
    print("all good boss")
