#encoding:utf-8
import os
from sayhello import app
dev_db='sqlite:///'+os.path.join(os.path.dirname(app.root_path),"data.db")
SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URI",dev_db)
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY=os.getenv("SECRET_KEY","secret string")