from flask import Blueprint, render_template
from mongoDB import recommendation_col

recommendation = Blueprint(
    'recommendation',
    __name__,
    static_folder='static',
    static_url_path='/recommendation',
    template_folder='templates'
)

@recommendation.route('/recommendation')
def index():
    recommendations = recommendation_col.find()
    return render_template('recommendation.html', recommendations=recommendations)

