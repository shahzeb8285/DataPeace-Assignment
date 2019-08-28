
from .. import db
import datetime


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"


    id = db.Column('ID', db.Integer, primary_key=True, index=True)
    first_name = db.Column("first_name",db.String, nullable=False)
    last_name = db.Column("last_name",db.String, nullable=False)
    company_name = db.Column("company_name",db.String, nullable=False)
    age = db.Column("age",db.Integer, nullable=False)
    city = db.Column("city",db.String, nullable=False)
    state = db.Column("state",db.String, nullable=False)
    zip = db.Column("zip",db.Integer, nullable=False)
    email = db.Column("email",db.String, nullable=False)
    web = db.Column("web",db.String, nullable=True)

   
    def __repr__(self):
        return "<User '{}'>".format(self.username)
