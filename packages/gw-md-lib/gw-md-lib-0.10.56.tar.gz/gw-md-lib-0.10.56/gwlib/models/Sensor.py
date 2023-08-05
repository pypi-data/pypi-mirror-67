from sqlalchemy import func

from . import db


class Sensor(db.Model):
    __tablename__ = "gw_sensor"

    sensor_id = db.Column(db.Integer, primary_key=True)
    hole_id = db.Column(db.Integer, db.ForeignKey('gw_hole.hole_id'))
    quadrant_id = db.Column(db.Integer, db.ForeignKey('gw_zone_quadrant.quadrant_id'))
    zone_id = db.Column(db.Integer, db.ForeignKey('gw_zone.zone_id'))
    location_id = db.Column(db.Integer, db.ForeignKey('gw_zone_location.location_id'))
    meid = db.Column(db.String(length=18), nullable=False)
    serial_number = db.Column(db.String(length=18), nullable=False)
    latitude = db.Column(db.DECIMAL(13, 10), nullable=True)
    longitude = db.Column(db.DECIMAL(13, 10), nullable=True)
    status = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    location_note = db.Column(db.String(120), nullable=False)
    location_desc = db.Column(db.String(150), nullable=False)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    time_updated = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)

