from application.model.entity.User import User
from application import db
import datetime

class CreateUserDAO():

    def create(self, nome, username, password, email, date, photo):
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        user = User(nome, username, password, email, date, photo)
        db.session.add(user)
        db.session.commit()
        return None
