from flask import Flask, request, abort
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

Database = [
    {'name':'Pepe', 'email':'pepe@correo.es'},
    {'name':'Juan', 'email':'juan@correo.es'},
    {'name':'Manuel', 'email':'manuel@correo.es'},
]

def find_user_byID(user_id):
    number_of_users = len(Database)
    if user_id > number_of_users:
        return -1
    else:
        return user_id-1


class Users(Resource):
    def get(self):
        return Database
    
    def post(self):
        data = request.json
        user = { 'name':data['name'], 'email':data['email']}
        Database.append(user)
        return user, 201

class User(Resource):
    def get(self, pk):
        user_id = find_user_byID(pk)
        if user_id != -1:
            return Database[user_id], 200
        else:
            abort(404, 'Not Found: User is not in database')
    
    def put(self, pk):
        data = request.json
        user_id = find_user_byID(pk)
        if user_id == -1:
            abort(404, 'Not Found: User is not in database')
        else:
            user = { 'name':data['name'], 'email':data['email']}
            Database[user_id] = user
        return user
    
    def delete(self, pk):
        user_id = find_user_byID(pk)
        if user_id == -1:
            abort(404, 'Not Found: User is not in database')
        else:
            user = Database[user_id]
            del Database[user_id]
        return user

api.add_resource(Users, '/api/')
api.add_resource(User, '/api/<int:pk>')

@api.route('/api/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)