from application import db, login_manager
from werkzeug.security import generate_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id = user_id).first()

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    foto = db.Column(db.String)
    data_nascimento = db.Column(db.Date)

    def __repr__(self):
        return "<User %r>" % self.username

    def __init__(self, nome, username, password, email, data_nascimento, foto):
        self.nome = nome
        self.username = username 
        self.password = generate_password_hash(password)
        self.email = email
        self.data_nascimento = data_nascimento
        self.foto = foto

    def get_password(self):
        return self.password



