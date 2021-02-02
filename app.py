from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)



mail_settings = {
    "MAIL_SERVER": 'smtp.office365.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS":True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": 'noreply@nelsonbrothers.net',
    "MAIL_PASSWORD": 'Pr1nt3rs!'
}

app.config.update(mail_settings)
mail = Mail(app)

@app.route('/')
def hello_world():
    msg = Message('Hello', sender = 'noreply@nelsonbrothers.net', recipients = ['shahzad.tabassum@yahoo.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run()
