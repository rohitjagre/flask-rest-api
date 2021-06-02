from datetime import datetime

from app.extensions import db


class TodoModel(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Todo(id={self.id}, content={self.content}, created_at={self.created_at})"
