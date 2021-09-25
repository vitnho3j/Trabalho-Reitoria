from application import app
from application.model.entity import User
from werkzeug.security import check_password_hash

class UserDAO():

    def verify_password(user, pwd):
        return check_password_hash(user.get_password(), pwd)

    