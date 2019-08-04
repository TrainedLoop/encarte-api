from .. import db
import datetime


class Encarte(db.Model):
    __tablename__ = 'encarte'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String,  nullable=False)
    brand_id = db.Column(db.String,  )
    uploaded_by = db.Column(db.String, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.String, nullable=False)






