from flask import Flask
from mongoDB import *

###### App setup
app = Flask(__name__)


app.secret_key = '123'
app.config.from_pyfile('settings.py')

###### Pages
## login
from pages.login.login import login

app.register_blueprint(login)
## MainPage

from pages.MainPage.MainPage import MainPage

app.register_blueprint(MainPage)

## history
from pages.history.history import history

app.register_blueprint(history)

## Feedback
from pages.Feedback.Feedback import Feedback

app.register_blueprint(Feedback)
## welcome
from pages.welcome.welcome import welcome


from pages.teachers.teachers import teachers

app.register_blueprint(teachers)
from pages.recommendation.recommendation import recommendation

app.register_blueprint(recommendation)

app.register_blueprint(welcome)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers

app.register_blueprint(page_error_handlers)
app.config.from_pyfile('settings.py')

