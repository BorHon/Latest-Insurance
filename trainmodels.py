#encoding:utf-8

# Just make the model simple in the first place
# In my view ,there are several mainly insurance suitable for our work
# A:the Children Health Insurance
# B:the family Health Insurance
# C:the specific disease Insurance,like the lung cancer Insurance
# D:the ordinary personal Insurance
# I know it may  simplify the whole question,but we can start form it and make it bigger .
from sayhello import db
class train_Information(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        Age = db.Column(db.Integer)
        Income = db.Column(db.Float())
        Height = db.Column(db.Float())
        Weight = db.Column(db.Float())
        Sex = db.Column(db.String())
        Marriage = db.Column(db.String())
        Deposit=db.Column(db.Float())
        Specific = db.Column(db.Boolean)
        Family_insured = db.Column(db.Boolean)
        Insurance = db.Column(db.String())

