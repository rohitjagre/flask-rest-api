from flask import Flask

from app.extensions import api, db
from app.todo.resources import Todos, TodosId

flask_app = Flask(__name__)
api.init_app(flask_app)

flask_app.config.from_object("config")
db.init_app(flask_app)


with flask_app.app_context():
    db.create_all()

import app.todo
