from models.base_model import BaseModel
import peewee as pw
import datetime
from flask_login import UserMixin



class User(BaseModel):
    username = pw.CharField(unique=True)
    email = pw.CharField(null=True, unique=True)
    password = pw.CharField(null=False)

    def validation(self):
        duplicate_useremail = User.get_or_none(User.email == self.email)


        if duplicate_useremail:
            self.errors.append('Email has been taken. Please try another email')  