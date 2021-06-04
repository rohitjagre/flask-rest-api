import pytest
from app import flask_app
from app.extensions import db


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True

    with flask_app.app_context():
        with flask_app.test_client() as client:
            yield client
