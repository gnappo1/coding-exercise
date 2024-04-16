#!/usr/bin/env python3

from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Hero, Power, HeroPower
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Code challenge</h1>'

#! Build a route for the endpoint GET /sorted-heroes
# * This route should be return a list of heroes sorted heroes in descending order by their super_name
# * Each hero inside the list will only display the following columns: id, name, super_name, hero_powers
# * Each nested hero_power inside their hero will only display the following columns: id, strength, hero_id, power_id
# * If no heroes exist, then an empty list is returned
#* In case of any failures, your API should never crash bu rather return the following response body: 
    #* {"error": "Could not process your request"}
    #* with status: 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)
