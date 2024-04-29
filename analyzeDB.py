import os
from mongoDB import *
from pymongo.server_api import ServerApi

# get your uri from .env file
uri = os.environ.get('DB_URI')

# create cluster
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster["mydatabase"]
pupils_col = mydatabase["pupils"]
lessons_col = mydatabase["lessons"]
feedback_col = mydatabase["feedback"]
recommendation_col = mydatabase["recommendation"]
teachers_col = mydatabase["teachers"]

def analyzeDB():
    pupils = list(pupils_col.find())
    print(pupils)

    lessons = list(lessons_col.find())
    print(lessons)

    feedbacks = list(feedback_col.find())
    print(feedbacks)

    recommendations = list(recommendation_col.find())
    print(recommendations)

    teachers = list(teachers_col.find())
    print(teachers)


