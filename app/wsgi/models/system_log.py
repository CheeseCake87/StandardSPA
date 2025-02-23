import sqlalchemy as s

from app.utilities.datetime_delta import DatetimeDeltaMC
from app.wsgi.extensions import db


class SystemLog(db.Model):
    __tablename__ = "system_log"

    # PriKey
    system_log_id = s.Column(s.Integer, primary_key=True)

    # Data
    system = s.Column(s.String(256), nullable=False)
    log = s.Column(s.String, nullable=True)

    # Tracking
    created = s.Column(s.DateTime)

    @classmethod
    def create(cls, system, log):
        ins_ = cls(system=system, log=log, created=DatetimeDeltaMC().datetime)
        db.session.add(ins_)
        db.session.commit()
