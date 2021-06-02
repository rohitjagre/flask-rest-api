from app.extensions import api, db
from app.todo.models import TodoModel
from app.todo.utils import (
    todo_model_fields,
    todos_id_patch_args,
    todos_post_args,
)
from flask_restful import Resource, abort, marshal_with


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
    def get(self, id):
        todo = TodoModel.query.get(id)
        if not todo:
            abort(404, message="Todo not found")
        return todo

    @marshal_with(todo_model_fields)
    def patch(self, id):
        todo = TodoModel.query.get(id)
        if not todo:
            abort(404, message="Todo not found")

        args = todos_id_patch_args.parse_args()
        for attr, value in args.items():
            if value:
                setattr(todo, attr, value)
        db.session.commit()
        return todo


api.add_resource(Todos, "/todos")
api.add_resource(TodosId, "/todos/<int:id>")
