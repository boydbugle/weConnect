# from flask import Flask,jsonify,abort,make_response,request,session
# from user import User,USERS
# import os
from flask import Flask

app = Flask(__name__,instance_relative_config=True)
#
# app.secret_key = os.urandom(24)
#
# users=User()

from app import views

app.config.from_object('config')
