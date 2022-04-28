from flask import Flask
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b641686bc9309119de8168d8196682a2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meditrack.db'
# db = SQLAlchemy(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'medicare.somaiya@gmail.com'
app.config['MAIL_PASSWORD'] = 'fhtxrfagpfiujunf'
app.config['MAIL_DEFAULT_SENDER'] = (
    'Meditrack Team', 'medicare.somaiya@gmail.com')
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_SUPPRESS_SEND'] = app.testing

from app import routes