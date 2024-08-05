from . import db
from datetime import datetime


class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_defined_id = db.Column(db.String(100), unique=True, nullable=False)
    request_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    data = db.Column(db.JSON, nullable=False)
