from flask import Blueprint, session
from flask import render_template, redirect, url_for

# homepage blueprint definition
welcome = Blueprint(
    'welcome',
    __name__,
    static_folder='static',
    static_url_path='/welcome',
    template_folder='templates'
)


# Routes
@welcome.route('/', methods=['GET', 'POST'])
def index():
    email = session.get('email')
    return render_template('welcome.html', email=email)
