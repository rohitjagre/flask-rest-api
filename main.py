from datetime import datetime

from flask import Flask
from flask_restful import Api, Resource, abort, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)


class TodoModel(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Todo(id={self.id}, content={self.content}, created_at={self.created_at})"


db.create_all()

todo_model_fields = {
    "id": fields.Integer,
    "content": fields.String,
    "created_at": fields.String,
}


todos_post_args = reqparse.RequestParser()
todos_post_args.add_argument(
    "content", type=str, help="content is required", required=True
)

todos_id_patch_args = reqparse.RequestParser()
todos_id_patch_args.add_argument(
    "content", type=str, help="content is required"
)
todos_id_patch_args.add_argument("id", type=int, help="id is required")
todos_id_patch_args.add_argument(
    "created_at", type=str, help="created_at is required"
)


class Todos(Resource):
    @marshal_with(todo_model_fields)
    def get(self):
        todos = TodoModel.query.all()
        return todos

    @marshal_with(todo_model_fields)
    def post(self):
        args = todos_post_args.parse_args()
        new_todo = TodoModel(content=args["content"])
        db.session.add(new_todo)
        db.session.commit()
        return (new_todo, 201)


class TodosId(Resource):
    @marshal_with(todo_model_fields)
    def get(self, id_):
        todo = TodoModel.query.get(id_)
        if not todo:
            abort(404, message="Todo not found")
        return todo

    @marshal_with(todo_model_fields)
    def patch(self, id_):
        todo = TodoModel.query.get(id_)
        if not todo:
            abort(404, message="Todo not found")

        args = todos_id_patch_args.parse_args()
        for attr, value in args.items():
            if value:
                setattr(todo, attr, value)
        db.session.commit()
        return todo


api.add_resource(Todos, "/todos")
api.add_resource(TodosId, "/todos/<int:id_>")

if __name__ == "__main__":
    app.run(debug=True)
