from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [{"name": "Nicholas", "age": 42, "occupation": "Software Engineer"},
         {"name": "Elvin", "age": 32, "occupation": "Doctor"},
         {"name": "Saad", "age": 31, "occupation": "Software Engineer"}
        ]

class User(Resource) :
    def get(self, name) :
        for user in users :
            if(name == user["name"]):
                return user, 200
        return "user not found", 404

    
    def delete(self, name) :
        return "{} is deleted".format(name), 200

class UserAdd(Resource) :
    def post(self) :
        parser = reqparse.RequestParser ()
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users :
            if(args["name"] ==  user["name"]) :
                return "User {} already added".format(args["name"]), 400
        
        user = {"name": args["name"], "age": args["age"],"occupation":args["occupation"]}
        users.append(user)

        return user, 200

class ListUser(Resource) :
    def get(self) :
        return users,200


api.add_resource(User, "/user/<string:name>")
api.add_resource(UserAdd,"/adduser")
api.add_resource(ListUser,"/listusers")

app.run(port=8080, debug=True)