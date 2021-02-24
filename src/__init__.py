import os
import sys
from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

#instantiate app
app = Flask(__name__)
api = Api(app)

#set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)

#print(app.config, file=sys.stderr)

#model
class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    fp = db.Column(db.String(264), unique=True) #absolute path
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, name, fp):
        self.name = name
        self.fp = fp

class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(Ping, '/ping')
