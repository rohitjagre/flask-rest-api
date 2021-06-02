from flask_restful import fields, reqparse

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
