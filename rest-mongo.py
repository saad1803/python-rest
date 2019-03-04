from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient
from bson.json_util import dumps
import json

client = MongoClient('localhost',27017)

database = client['test_db1']

app = Flask(__name__)
api = Api(app)


class MongoFindAll(Resource) :
    def get(self) :
        pets = dumps(database.pets.find())
        return pets,200

class MongoAddPet(Resource) :
    def post(self) :
        data =json.loads(request.data)
        
        database.pets.insert_one({
            "name" : data['name'],
            "species" : data['species'],
            "breed" : data['breed']
        })

        return data["name"],200

class PetByName(Resource) :
    def get(self,name) :
        try :
            data = database.pets.find({"name": name})
            # print json.load(str(data))
            return dumps(data),200
        except Exception, e:
            return dumps({'error',str(e)})




api.add_resource(MongoFindAll,"/getAllPets")
api.add_resource(MongoAddPet,"/addPet")
api.add_resource(PetByName, "/getPetByName/<string:name>")

app.run(port=8080, debug=True)