#encoding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,FloatField,SelectField,RadioField
from wtforms.validators import  DataRequired,Length

class HelloForm(FlaskForm):
    Card_Id=StringField("Your Bank Card Number",validators=[DataRequired()])
    Age=FloatField("Age", validators=[DataRequired()])
    Income=FloatField("Salary")
    Deposit = FloatField("Deposit")
    Height = FloatField("Height", validators=[DataRequired()])
    Weight=FloatField("Weight",validators=[DataRequired()])
    Marriage = SelectField('Marriage', choices=[('married', 'married'), ('unmarried', 'unmarried'), ("divorced", "divorced")])
    Sex = SelectField('Sex', choices=[('Male','Male'), ('Female','Female'),("Unknown","Unknown")], validators=[DataRequired()])
    Critical_illness= SelectField('Critical illness', choices=[('Yes', 'Yes'), ('No', 'No'), ("Unknown", "Unknown")],validators=[DataRequired()])
    Family_insured=SelectField('Family insured', choices=[('Yes', 'Yes'), ('No', 'No')],validators=[DataRequired()])
    submit=SubmitField()
