from flask import Response, jsonify, request
from sqlalchemy.orm.exc import NoResultFound

from main.models.task import Task


class TaskAPI:
    @staticmethod
    def list_tasks():
        try:
            tasks = Task.get_all()
            return jsonify({"result": [task.to_dict() for task in tasks]}), 200
        except Exception as ex:
            return jsonify({"result": f"Unknown reason, ex: {ex}"}), 500

    @staticmethod
    def create_task():
        try:
            request_json = request.get_json()
            name = request_json.get("name")
            new_task = Task(name=name).create()
            return jsonify({"result": new_task.to_dict()}), 201
        except Exception as ex:
            return jsonify({"result": f"Unknown reason, ex: {ex}"}), 500

    @staticmethod
    def update_task(id: int):
        request_json = request.get_json()
        name, status = request_json.get("name"), request_json.get("status")
        try:
            update_task = Task(name=name, status=status).update(id)
            return jsonify({"result": update_task.to_dict()}), 200
        except NoResultFound:
            return jsonify({"result": f"Task id {id} is not found"}), 422
        except Exception as ex:
            return jsonify({"result": f"Unknown reason, ex: {ex}"}), 500

    @staticmethod
    def delete_task(id: int):
        try:
            Task.delete(id)
            return Response(status=200)
        except NoResultFound:
            return jsonify({"result": f"Task id {id} is not found"}), 422
        except Exception as ex:
            return jsonify({"result": f"Unknown reason, ex: {ex}"}), 500
