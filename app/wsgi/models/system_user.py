import sqlalchemy as s

from app.wsgi.extensions import db


class SystemUser(db.Model):
    __tablename__ = "system_user"

    # PriKey
    system_user_id = s.Column(s.Integer, primary_key=True)

    # Data
    username = s.Column(s.String(256), nullable=False)
    display_name = s.Column(s.String(64), nullable=False)

    # Contact
    email = s.Column(s.String(256), nullable=True)
    sms = s.Column(s.String(18), nullable=True)

    # Private
    salt = s.Column(s.String(4), nullable=False)
    password = s.Column(s.String(512), nullable=False)
    private_key = s.Column(s.String(256), nullable=False)

    # Access Level
    access = s.Column(s.Integer, default=1)
    # 10 = Super Administrator
    # 9 = Administrator
    # 1 = User

    disabled = s.Column(s.Boolean, default=False)
    deleted = s.Column(s.Boolean, default=False)

    # Tracking
    created = s.Column(s.DateTime)
