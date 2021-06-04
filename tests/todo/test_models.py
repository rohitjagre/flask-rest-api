from app.todo.models import TodoModel


def test_create():
    content = "Test content"
    todo = TodoModel(content=content)
    print(f"{todo!r}")
    assert todo.content == content
