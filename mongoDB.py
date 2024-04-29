import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://tal:419@cluster0.yef9fkf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster["mydatabase"]
pupils_col = mydatabase["pupils"]
lessons_col = mydatabase["lessons"]
recommendation_col = mydatabase["recommendation"]
teachers_col = mydatabase["teachers"]
feedback_col = mydatabase["feedback"]
my_list = [
    {'id': '12345678', 'first_name': 'אבי', 'last_name': 'יוחאי', 'age': 30, 'email': 'avi@example.com',
     'password': '12345646'},
    {'id': '87654321', 'first_name': 'שירה', 'last_name ': 'כהן', 'age': 25, 'email': 'shira@example.com',
     'password': 'abcdef00'},
    {'id': '67890123', 'first_name': 'מיכל', 'last_name': 'שוורץ', 'age': 22, 'email': 'michal@example.com',
     'password': 'michal789'},
    {'id': '45678901', 'first_name': 'רונן', 'last_name': 'בן-דוד', 'age': 27, 'email': 'ronen@example.com',
     'password': 'ronen654'},
    {'id': '01234567', 'first_name': 'אילה', 'last_name': 'כהן', 'age': 29, 'email': 'eila@example.com',
     'password': 'eila321q'},
]
pupils_col.insert_many(my_list)
my_lessons = [
    {'id': '1', 'teacher': 'יואב כהן', 'pupil': 'avi@example.com', 'subject': 'מתמטיקה', 'type': 'זום', 'date': '2/1/2023'},
    {'id': '2', 'teacher': 'גל רוני', 'pupil': 'shira@example.com', 'subject': 'אנגלית', 'type': 'פרונטלי', 'date': '12/1/2023'},
    {'id': '3', 'teacher': 'יואב כהן', 'pupil': '', 'ronen@example.com': 'מתמטיקה', 'type': 'זום', 'date': '20/9/2023'},
    {'id': '4', 'teacher': 'גל רוני', 'pupil': 'avi@example.com', 'subject': 'אנגלית', 'type': 'פרונטלי', 'date': '12/2/2023'},
    # Additional lessons for 'avi@example.com'
    {'id': '5', 'teacher': 'מאיה לוי', 'pupil': 'avi@example.com', 'subject': 'היסטוריה', 'type': 'זום', 'date': '5/3/2023'},
    {'id': '6', 'teacher': 'דן כהן', 'pupil': 'avi@example.com', 'subject': 'פיזיקה', 'type': 'פרונטלי', 'date': '15/3/2023'},
    {'id': '7', 'teacher': 'נועם כהן', 'pupil': 'avi@example.com', 'subject': 'כימיה', 'type': 'פרונטלי', 'date': '25/3/2023'},
    # Additional lessons for 'shira@example.com'
    {'id': '8', 'teacher': 'אלון כהן', 'pupil': 'shira@example.com', 'subject': 'ספרות', 'type': 'זום', 'date': '7/4/2023'},
    {'id': '9', 'teacher': 'רותם כהן', 'pupil': 'shira@example.com', 'subject': 'ביולוגיה', 'type': 'פרונטלי', 'date': '17/4/2023'},
    {'id': '10', 'teacher': 'ניב כהן', 'pupil': 'shira@example.com', 'subject': 'גאוגרפיה', 'type': 'זום', 'date': '27/4/2023'},
    # Additional lessons for 'ronen@example.com'
    {'id': '11', 'teacher': 'יעקב כהן', 'pupil': 'ronen@example.com', 'subject': 'אזרחות', 'type': 'זום', 'date': '9/5/2023'},
    {'id': '12', 'teacher': 'שלומי כהן', 'pupil': 'ronen@example.com', 'subject': 'תנ"ך', 'type': 'פרונטלי', 'date': '19/5/2023'},
    {'id': '13', 'teacher': 'טל כהן', 'pupil': 'ronen@example.com', 'subject': 'אנגלית', 'type': 'פרונטלי', 'date': '29/5/2023'},
    # Lessons for 'michal@example.com'
    {'id': '14', 'teacher': 'דוד כהן', 'pupil': 'michal@example.com', 'subject': 'פסיכולוגיה', 'type': 'פרונטלי', 'date': '8/6/2023'},
    {'id': '15', 'teacher': 'שירה כהן', 'pupil': 'michal@example.com', 'subject': 'אמנות', 'type': 'פרונטלי', 'date': '18/6/2023'},
    {'id': '16', 'teacher': 'מיכאל כהן', 'pupil': 'michal@example.com', 'subject': 'מוזיקה', 'type': 'פרונטלי', 'date': '28/6/2023'},
    # Lessons for 'eila@example.com'
    {'id': '17', 'teacher': 'נעמה כהן', 'pupil': 'eila@example.com', 'subject': 'גאוגרפיה', 'type': 'פרונטלי', 'date': '9/7/2023'},
    {'id': '18', 'teacher': 'ליאור כהן', 'pupil': 'eila@example.com', 'subject': 'היסטוריה', 'type': 'פרונטלי', 'date': '19/7/2023'},
    {'id': '19', 'teacher': 'מיה כהן', 'pupil': 'eila@example.com', 'subject': 'אנגלית', 'type': 'פרונטלי', 'date': '29/7/2023'},
]

lessons_col.insert_many(my_lessons)

my_teachers = [
    {'teacher': 'שירה יוחאי', 'subject': 'אמנות', 'location': 'כל הארץ', 'vetek': '12'},
    {'teacher': 'מיכאל אורי', 'subject': 'מוזיקה', 'location': 'כל הארץ', 'vetek': '12'},
    {'teacher': 'נעמה אור', 'subject': 'גאוגרפיה', 'location': 'צפון', 'vetek': '19'},
    {'teacher': 'ליאור כהן', 'subject': 'היסטוריה', 'location': 'צפון', 'vetek': '19'},
    {'teacher': 'מיה כהן', 'subject': 'אנגלית', 'location': 'צפון', 'vetek': '12'}
]
teachers_col.insert_many(my_teachers)

my_list = [
    {'pupil': 'אבי יוחאי', 'feedback': 'השיעורים תרמו לי רבות ובעזרתם הצלחתי לעבור את מבחני הבגרות!'},
    {'pupil': 'שירה כהן', 'feedback': 'המורים באתר מעולים ובעזרתם הצלחתי לעבור את מבחני הבגרות בהצלחה רבה!'},
    {'pupil': 'רונן בן דוד', 'feedback': 'תודה למורה שלי יואחי אורן על העזרה הרבה בשיעורי המתמטיקה!'},
    {'pupil': 'מיכל שוורץ', 'feedback': 'השיעורים תרמו לי רבות והמורים היו ממש מקצועיים!'},
    {'pupil': 'יוכי אטויר', 'feedback': 'השיעורים היו מעניינים ועזרו לי להבין את החומר!'},

]
recommendation_col.insert_many(my_list)

def create_pupil(email, password, first_name, last_name, id_number, age):
    new_user = {
        'email': email,
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
        'id': id_number,  # Renamed 'id' to 'id_number'
        'age': age
    }
    print(new_user)
    pupils_col.insert_one(new_user)



def check_registered(email):
    if get_user_by_email(email):
        return True
    return False


def get_user_by_email(email):
    return pupils_col.find_one({'email': email})


def checkPupil(email, password):
    pupil = pupils_col.find_one({'email': email})
    if pupil is None:
        return False
    if pupil['password'] != password:
        return False
    return True


def create_feedback(id_number, rating, feedback):
    new_feedback = {
        'id': id_number,
        'rating': rating,
        'feedback': feedback
    }
    feedback_col.insert_one(new_feedback)
