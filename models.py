from email.policy import default
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Todo(db.Model):
    """Todo Model"""

    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, default=False)

    def serialize(self):
        """Turns a db model object into a dict in order to jsonify it and return json to the requestor"""
        return {"id": self.id, "title": self.title, "done": self.done}

    def __repr__(self):
        return f"<Todo {self.id} title={self.title} done={self.done}"
