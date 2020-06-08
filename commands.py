# -*- coding: utf-8 -*-
# A:the Children Health Insurance
# B:the family Health Insurance
# C:the specific disease
# Insurance,like the lung cancer Insurance
# D:the ordinary personal health Insurance
# E:the cheapest insurance --accident Insurance, for people who are poor and keep low deposit as well as  a nice BMI

import click
from sayhello import app, db
from sayhello.models import Information
from sayhello.trainmodels import train_Information
from faker import Faker


def produce_train():
    fake = Faker()
    marriage_choice = ["married", "unmarried", "divorced"]
    sex_choice = ["Male", "Female", "UnKnown"]
    age = fake.random_int(min=0, max=50)
    specific = (fake.random_int(min=0, max=100000) % 37 == 1)
    Family_insured = 0
    if age <= 18:
        income = 0
        marriage = "unmarried"
        Family_insured = 0
    else:
        income = fake.random_int(min=0, max=30000)
        marriage = marriage_choice[fake.random_int(min=0, max=99) % 3]
        Family_insured = fake.random_int(min=0, max=100000) % 3== 0

    sex = sex_choice[fake.random_int(min=0, max=99) % 3]
    height = fake.random_int(min=140, max=190)
    weight = fake.random_int(min=30, max=100)
    BMI = weight / (height ** 2)
    insurance = ""
    deposit = income * fake.random_int(min=0, max=10)
    if age < 12:
        insurance = insurance + "A"
    if specific:
        insurance = insurance + "C"
    if marriage == "married" and sex == "Male":
        if not Family_insured and age < 45:
            insurance = insurance + "B"
    if insurance == "":
        if deposit < 5000 and (BMI < 23.9 and BMI > 18.5):
            insurance = "E"
        else:
            insurance = "D"

    return age, income, marriage, sex, height, weight, deposit, specific, Family_insured, insurance


@app.cli.command()
def forges(count=2000):
    """Generate training data."""
    click.echo('Working...')
    for i in range(count):
        age, salary, marriage, sex, height, weight, deposit, specific, family_insured, insurance = produce_train()
        train_information = train_Information(
            Age=age,
            Income=salary,
            Marriage=marriage,
            Height=height,
            Weight=weight,
            Sex=sex,
            Insurance=insurance,
            Deposit=deposit,
            Specific=specific,
            Family_insured=family_insured
        )
        # print(train_information.Insurance)
        db.session.add(train_information)
    db.session.commit()
    click.echo('Created %d fake messages.' % count)


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')
