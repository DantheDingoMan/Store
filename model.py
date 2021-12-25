from os import name
from config import db, mm

class items(db.Model):
    __tablename__ = "ITEM"
    itemname = db.Column(db.String, primary_key = True)
    price = db.Column(db.Float)
    description = db.Column(db.String)




class itemsSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = items
        load_instance = True

