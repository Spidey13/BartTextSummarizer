from datetime import datetime

from app import db, login_manager
# from flask_login import UserMixin


class Data(db.model):
    id = db.Column(db.Integer, primary_key=True)
    transcripts = db.Column(db.String(1000), default=None, nullable=True)
    text = db.Column(db.String(1000), default=None)
    summarized_text = db.Column(db.String(500), default=None)


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     date = db.Column(db.DateTime, default=datetime.now, nullable=False)
#     blood = db.Column(db.String(10), nullable=False)
#     meds = db.relationship('Medicines', backref='user', lazy=True)


#     def __repr__(self):
#         return f"User('{self.name}', '{self.email}','{self.blood}','{self.date}')"

# class Medicines(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     medname = db.Column(db.String(20), nullable=False)
#     power = db.Column(db.String(10), nullable=True)
#     morning = db.Column(db.Boolean, default=False, nullable=False)
#     afternoon = db.Column(db.Boolean, default=False, nullable=False)
#     night = db.Column(db.Boolean, default=False, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"medicines('{self.medname}','{self.morning}','{self.afternoon}','{self.night}')"
