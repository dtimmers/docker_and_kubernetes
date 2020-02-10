from app_api import db


class FibonacciIndex(db.Model):
    __tablename__ = 'indices'

    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.Integer, nullable=False, unique=True)