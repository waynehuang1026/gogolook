from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound

db = SQLAlchemy()


class Task(db.Model):
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    status = db.Column(db.SmallInteger, default=0)

    def __init__(self, name: str, status: int = 0):
        self.name = name
        self.status = status

    def to_dict(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, id: int):
        task = self.query.get(id)
        if not task:
            raise NoResultFound
        task.name, task.status = self.name, self.status
        return task

    @classmethod
    def delete(cls, id: int):
        task = cls.query.get(id)
        if not task:
            raise NoResultFound
        db.session.delete(task)
        db.session.commit()
