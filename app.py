from flask import Flask
from flask_mail import Message, Mail



app = Flask(__name__)

app.secret_key = ''


mail = Mail()

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = ''
app.config["MAIL_PASSWORD"] = app.secret_key

mail.init_app(app)

