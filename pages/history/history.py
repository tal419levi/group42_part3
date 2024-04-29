from flask import Blueprint, session
from flask import render_template, redirect, url_for

from mongoDB import *

# homepage blueprint definition
history = Blueprint(
    'history',
    __name__,
    static_folder='static',
    static_url_path='/history',
    template_folder='templates'
)


# Routes
@history.route('/history')
def index():
        email = session.get('email')
        lessons = lessons_col.find({'pupil':email})
        if lessons:
            lesson_data = []
            displayed_lessons = set()  # רשימת השיעורים שכבר הוצגו
            for lesson in lessons:
                lesson_id = lesson['id']
                if lesson_id not in displayed_lessons:  # בודקים האם השיעור כבר הוצג
                    teacher_name = lesson.get('teacher', 'Teacher Not Found')
                    subject = lesson.get('subject', 'Subject Not Found')
                    lesson_type = lesson.get('type', 'Type Not Found')
                    date = lesson.get('date', 'Date Not Found')
                    lesson_data.append(
                        {'teacher': teacher_name, 'subject': subject, 'lesson_type': lesson_type, 'date': date})
                    displayed_lessons.add(lesson_id)  # מוסיפים את השיעור לרשימת השיעורים שכבר הוצגו
            return render_template('history.html', lessons=lesson_data)
        else:
            return 'No Lessons Found'
