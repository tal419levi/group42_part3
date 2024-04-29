from flask import Blueprint, session
from flask import render_template, redirect, url_for
from mongoDB import *


# homepage blueprint definition
teachers = Blueprint(
    'teachers',
    __name__,
    static_folder='static',
    static_url_path='/teachers',
    template_folder='templates'
)


# Routes
@teachers.route('/teachers')
def index():
    teachers = teachers_col.find()
    return render_template('teachers.html', teachers=teachers)