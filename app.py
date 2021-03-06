from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth
from routes.todolist import todolist
from routes.orders import orders
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from utils.loginManagerService import login_manager
from utils.db import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)
Bcrypt(app)
login_manager.init_app(app)
Migrate(app, db)

app.register_blueprint(auth)
app.register_blueprint(todolist)
app.register_blueprint(orders)
