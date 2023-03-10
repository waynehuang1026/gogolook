import os

import connexion

from main.models.task import db

db_host = os.environ.get("DB_HOST", "localhost")
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:root@{db_host}:3306/demo"


def create_app():
    connexion_app = connexion.App(__name__, specification_dir="./")
    connexion_app.add_api("swagger.yaml")
    return connexion_app.app


if __name__ == "__main__":
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000)
