import connexion

from config import SQLALCHEMY_DATABASE_URI
from main.models.task import db

connexion_app = connexion.App(__name__, specification_dir="./")
connexion_app.add_api("swagger.yaml")

app = connexion_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000)
