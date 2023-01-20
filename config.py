import os

SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI", "mysql+pymysql://root:root@localhost:3306/demo"
)
