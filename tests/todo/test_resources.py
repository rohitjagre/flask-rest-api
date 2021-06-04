from random import randint

from tests.test_app import client


def test_todos_post(client):
    content = "test_content"
    resp = client.post("/todos", json={"content": content})
    assert resp.status_code == 201
    assert resp.get_json()["content"] == content


def test_todos_get(client):
    content = "test_content"
    resp = client.post("/todos", json={"content": content})
    todo_id = resp.get_json()["id"]
    resp = client.get("/todos")
    assert resp.status_code == 200
    resp_json = resp.get_json()
    assert len(list(filter(lambda e: e["id"] == todo_id, resp_json))) == 1


def test_todos_id_get_notfound(client):
    resp = client.get(f"/todos/{randint(97, 345)}")
    assert resp.status_code == 404


def test_todos_id_get(client):
    content = "test_content"
    resp = client.post("/todos", json={"content": content})
    todo_id = resp.get_json()["id"]

    resp = client.get(f"/todos/{todo_id}")
    assert resp.status_code == 200
    resp_json = resp.get_json()
    assert resp_json["id"] == todo_id
    assert resp_json["content"] == content


def test_todos_id_patch_notfound(client):
    content = "test_content"
    resp = client.patch(
        f"/todos/{randint(97, 345)}", json={"content": content}
    )
    assert resp.status_code == 404


def test_todos_id_patch(client):
    content = "patched test_content"
    resp = client.post("/todos", json={"content": content})
    todo_id = resp.get_json()["id"]

    resp = client.patch(f"/todos/{todo_id}", json={"content": content})
    assert resp.status_code == 200
    print(resp.get_json())
