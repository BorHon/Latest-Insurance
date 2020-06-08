#encoding:utf-8
from sayhello import db
from datetime import datetime
#encoding:utf-8
class Information(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Age=db.Column(db.Integer)
    Income=db.Column(db.Float())
    Height=db.Column(db.Float())
    Weight=db.Column(db.Float())
    Marriage = db.Column(db.String())
    Card_ID=db.Column(db.String())
    Sex=db.String(db.String())



