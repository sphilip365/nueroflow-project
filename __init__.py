import datetime
import shelve
from flask import Flask, request, jsonify, g
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("moods.db")
    return db

class Mood(Resource):

    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        obj = []

        if login() != 0:
            for key in keys:
                obj.append(shelf[key])

            return {'message': 'Success', 'data': obj}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('mood', required=True)

        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifier']] = args

 def login():
    auth = request.authorization
    if auth and auth.password == "password":
        token = [{"user" : auth.username, "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}]
        return jsonify({"token" : token})
    return 0

api.add_resource(Mood, '/moods')
