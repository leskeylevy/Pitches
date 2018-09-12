from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    pitch = db.relationship('Pitch', backref='user', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitch'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String)
    title = db.Column(db.String)
    content = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls, category):
        pitch = Pitch.query.filter_by(category=category).all()
        return pitch

    @classmethod
    def get_pitch_order(cls):
        pitch = Pitch.query.order_by('id').all()
        return pitch


    def __repr__(self):
        return f'Pitch {self.title}'
