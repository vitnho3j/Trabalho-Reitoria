from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__, template_folder = 'C:\\Users\Vitor\Desktop\\Trabalho Reitoria\\Ambiente_Virtual\\application\\view\\templates', static_folder='C:\\Users\\Vitor\Desktop\\Trabalho Reitoria\\Ambiente_Virtual\\application\\view\\statics')
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from application.model.entity import User
from application.controllers import post, createUser, home, login