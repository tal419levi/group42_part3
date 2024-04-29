from flask import Blueprint, session
from flask import render_template, redirect, url_for


# homepage blueprint definition
MainPage = Blueprint(
    'MainPage',
    __name__,
    static_folder='static',
    static_url_path='/MainPage',
    template_folder='templates'
)


# Routes
@MainPage.route('/MainPage',methods=['GET', 'POST'])
def index():
    user_email = session.get('email')
    return render_template('MainPage.html', user_email=user_email)
