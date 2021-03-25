from . import db

class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(95))
    description = db.Column(db.String(1000))
    bedroom = db.Column(db.String(30))
    bathroom = db.Column(db.String(30))     
    price = db.Column(db.String(100))
    ptype = db.Column(db.String(25))
    location = db.Column(db.String(300))
    photo = db.Column(db.String(300))

    def __init__(self, description, bedroom, bathroom, price, ptype, location, photo):
        self.title = title
        self.description = description
        self.bedroom = bedroom
        self.bathroom = bathroom 
        self.price = price  
        self.type = ptype  
        self.location = location
        self.photo = photo    