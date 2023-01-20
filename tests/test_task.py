import json
import os

import pytest

from sqlalchemy.orm.exc import NoResultFound

from app import create_app
from main.models.task import db

db_host = os.environ.get("DB_HOST", "localhost")
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:root@{db_host}:3306/test"


@pytest.fixture()
def app():
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["TESTING"] = True
    db.init_app(app)
    with app.app_context():
        db.create_all()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_list_tasks(client):
    client.post("/task", json={"name": "123"})
    resp = client.get("/tasks")
    status_code, data = resp.status_code, json.loads(resp.data)["result"]
    assert status_code == 200 and data


def test_create_task(client):
    resp = client.post("/task", json={"name": "123"})
    status_code, data = resp.status_code, json.loads(resp.data)["result"]
    assert status_code == 201
    assert data["name"] == "123" and data["status"] == 0


def test_update_task(client):
    resp = client.post("/task", json={"name": "123"})
    id = json.loads(resp.data)["result"]["id"]
    resp = client.put(f"/task/{id}", json={"name": "456", "status": 1})
    status_code, data = resp.status_code, json.loads(resp.data)["result"]
    assert status_code == 200
    assert data["name"] == "456" and data["status"] == 1


def test_update_task_failure(client):
    id = 1000000
    resp = client.put(f"/task/{id}", json={"name": "456", "status": 1})
    status_code, data = resp.status_code, json.loads(resp.data)["result"]
    assert status_code == 422 and data == f"Task id {id} is not found"


def test_delete_task(client):
    resp = client.post("/task", json={"name": "123"})
    id = json.loads(resp.data)["result"]["id"]
    resp = client.delete(f"/task/{id}")
    status_code, data = resp.status_code, resp.data
    assert status_code == 200 and not data


def test_delete_task_failure(client):
    id = 1000000
    resp = client.delete(f"/task/{id}")
    status_code, data = resp.status_code, json.loads(resp.data)["result"]
    assert status_code == 422 and data == f"Task id {id} is not found"
