from app import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/manage.db'


class User(db.Model):
    user = db.Column(db.String, primary_key=True)
    income = db.Column(db.Integer, nullable=False)
    food_ex = db.Column(db.Integer, nullable=False)
    food_st = db.Column(db.Integer, nullable=False)
    daily_ex = db.Column(db.Integer,  nullable=False)
    daily_st = db.Column(db.Integer,  nullable=False)
    hobby_ex = db.Column(db.Integer,  nullable=False)
    hobby_st = db.Column(db.Integer,  nullable=False)
    last_ex = db.Column(db.Integer,  nullable=False)
    rent_cost = db.Column(db.Integer, nullable=False)
    scholar = db.Column(db.Integer, nullable=False)
    utility_cost = db.Column(db.Integer, nullable=False)
    other = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user

def return_data(user_id):
    data = User.query.filter_by(user='tfjkv').first()
    return data
