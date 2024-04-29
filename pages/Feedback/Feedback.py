from flask import Blueprint, request, render_template, redirect, url_for
from mongoDB import create_feedback

Feedback = Blueprint(
    'Feedback',
    __name__,
    static_folder='static',
    static_url_path='/Feedback',
    template_folder='templates'
)

# Counter for generating unique IDs
feedback_counter = 0


@Feedback.route('/Feedback', methods=['GET', 'POST'])
def index():
    global feedback_counter

    if request.method == 'POST':
        feedback_counter += 1  # Increment the counter for each new feedback submission
        id_number = feedback_counter  # Use the counter value as the ID
        rating = request.form.get('rating')
        feedback = request.form.get('feedback')

        if not feedback or not rating or rating == 'בחר':
            return render_template('Feedback.html', error="אנא מלא את הטופס")

        create_feedback(id_number, rating, feedback)

        return render_template('Feedback.html', success="הערכה נשלחה, תודה רבה!")

    # Render the feedback form template
    return render_template('Feedback.html')

