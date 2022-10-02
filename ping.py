import json
from multiprocessing import AuthenticationError
import os
from flask import Flask, jsonify 
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_httpauth import HTTPDigestAuth
import random


URL = 'http://127.0.0.1:5004/'

#create a Flask application instance called app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secrey key here'
auth = HTTPDigestAuth()


users = {"vcu" : "rams"}

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message': 'Page Doesnt Work'}), 404

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/ping', methods=['GET'])
@auth.login_required
def ping():
    r = requests.get('http://127.0.0.1:5000/pong', auth=('vcu', 'rams'))
    r_temp = r.elapsed.total_seconds()
    pingpong_t = r_temp * 1000
    return jsonify(pingpong_t)
