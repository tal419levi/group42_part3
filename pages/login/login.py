from flask import Blueprint, request, session, flash, redirect, url_for, render_template
from mongoDB import checkPupil

# homepage blueprint definition
login = Blueprint(
    'login',
    __name__,
    static_folder='static',
    static_url_path='/login',
    template_folder='templates'
)


@login.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if checkPupil(email, password):
            session['email'] = email
            return redirect(url_for('MainPage.index'))
        else:
            flash('Invalid email or password', 'error')
    return render_template('login.html')


@login.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('login.index'))

