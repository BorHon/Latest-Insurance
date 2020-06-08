#encoding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
#############这是什么啊，moment
from flask_migrate import Migrate
from flask_moment import Moment
app=Flask("sayhello")
app.config.from_pyfile("settings.py")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
db=SQLAlchemy(app)
moment=Moment(app)
bootstrap = Bootstrap(app)
migrate=Migrate(app,db)
#####################在_init_.py中把模块注册了
from sayhello import views,errors,commands,recommend
