#encoding:utf-8
from flask  import flash,url_for,render_template,redirect
from sayhello import app,db
from sayhello.forms import  HelloForm
from sayhello.models import Information
from sayhello.recommend import  recommned_model
@app.route("/",methods=["GET","POST"])
def index():
    insurance=""
    Card_ID=""
    form=HelloForm()
    if form.validate_on_submit():
        Age=form.Age.data
        Income=form.Income.data
        Weight=form.Weight.data
        Height=form.Height.data
        Marriage=form.Marriage.data
        Sex=form.Sex.data
        Card_ID=form.Card_Id.data
        if (form.Critical_illness.data == "Yes"):
            Specific = 1
        else:
            Specific = 0
        Deposit=form.Deposit.data
        if (form.Family_insured.data == "Yes"):
            Insured = 1
        else:
            Insured = 0
        print("No."+Card_ID +" customer" + " is waiting for your advice")
        flash('Your message has been updated')
        insurance=recommned_model.get_recommendation(Age,Income,Weight,Height,Deposit,Specific,Insured,Sex,Marriage)
        print(insurance)
        return render_template("index.html", form=form, recommendation=insurance, card_ID=Card_ID)
    if not form.validate_on_submit():
        print(form.errors)
    return render_template("index.html",form=form,recommendation=insurance,card_ID=Card_ID)


