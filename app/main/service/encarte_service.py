import uuid
import datetime

from app.main import db
from app.main.model.encarte import Encarte


def save_new_encarte(data):
    new_encarte = Encarte(image=data['image'],
        uploaded_by=data['user_id'],
        brand_id=data['brand_id'],
        create_date=datetime.datetime.now(),
        start_date=datetime.datetime.strptime(data['start_date'],"%Y-%m-%dT%H:%M:%S.%fZ"),
        end_date=datetime.datetime.strptime(data['end_date'],"%Y-%m-%dT%H:%M:%S.%fZ"),
        state='NEW')

    save_changes(new_encarte)

    
def get_encartes(page=1, per_page=10):
    return Encarte.query.all()



def save_changes(data):
    db.session.add(data)
    db.session.commit()

