from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'


def send_email():
    import smtplib

    gmail_user = "kkzxak47@gmail.com"
    gmail_pwd = "bl58tphppeGMAIL"
    FROM = 'kkzxak47@gmail.com'
    TO = ['kkzxak47@163.com']  # must be a list
    SUBJECT = "Digital Ocean Server Error"
    TEXT = "Testing sending mail using gmail servers"

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        # server = smtplib.SMTP(SERVER)
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(gmail_user, gmail_pwd)
        # server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        # server.ehlo()
        # server.starttls()
        # server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        # server.quit()
        server.close()
        app.logger.error('successfully sent the mail')
    except:
        app.logger.error("failed to send mail")

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler(
        (MAIL_SERVER, MAIL_PORT),
        '{}@gmail.com'.format(MAIL_USERNAME), ADMINS,
        'microblog failure', credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

    send_email()

    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')

from app import views, models
