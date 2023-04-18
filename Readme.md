# Webs y APIs Python

## Flask

Flask es un framework "liviano" para desarrollo de aplicaciones Web con Python. https://flask.palletsprojects.com/en/2.2.x/

```
(virtual_env)$ pip install flask
```

Ejemplo:

### Estructura del directorio

```
app
  |- static
  |       |- css
  |       |    | (Estilos CSS)
  |       |    `- main.css              
  |       |- img
  |       |    | (imágenes)
  |       |    `- web.png    
  |       |- js (ficheros JS)
  |
  |- templates
  |          | (Plantillas HTML)
  |          `- index.html
  `- web.py
```

Fichero web.py
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def saluda():
    return render_template('index.html', msg="Hola Mundo!")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
```

Fichero index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Web App</title>
    <link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='css/main.css') }}" />
</head>
<body>
    <h1> {{ msg }}</h1>
    <img src="{{ url_for('static',filename='img/web.png') }}" />
</body>
</html>
```


## Flask-RESTX

Flask-RESTX es un framework que facilita el desarrollo de APIs RESTful con Flask. https://flask-restx.readthedocs.io/en/latest/quickstart.html

```
(virtual_env)$ pip install flask-restx
```

Fichero api.py

```python
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
```

Para probar la API usar:

- Insomnia: https://insomnia.rest/download

- Postman: https://www.postman.com/downloads/



## Base de datos

https://www.sqlalchemy.org/


## Desplegando en Pythonanywhere

https://blog.pythonanywhere.com/121/