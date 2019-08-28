import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
  
    new_user = User(
        email=data['email'],
        first_name = data['first_name'],
        last_name = data['last_name'],
        age = data['age'],
        company_name = data['company_name'],
        city = data['city'],
        state = data['state'],
        web = data['web'],
        zip = data['zip'],

    )
    save_changes(new_user)
    response_object = {}
    return response_object, 201
   

def get_all_users():
    return User.query.all()


def get_a_user(id):
    return User.query.filter_by(id=id).first()

def delete_a_user(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

