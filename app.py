#python -m flask run
import json
from flask import Flask, request, render_template
from Data.Access.UserAccess import UserAccess
from Util.JSONEncoder import JSONEncoder
from Entities.User import User
from Util.DateTimeEncoder import DateTimeEncoder

app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_users():
    userAccess = UserAccess()
    users = userAccess.GetUsers()
    return JSONEncoder().encode(users)

@app.route('/<id>', methods=["GET"])
def get_user(id):
    userAccess = UserAccess()
    user = userAccess.GetUser(id)
    return JSONEncoder().encode(user)

@app.route('/', methods=["POST"])
def insert_user():
    userAccess = UserAccess()
    user = json.loads(json.dumps(request.json, cls=DateTimeEncoder), object_hook=User)
    result = userAccess.InsertUser(user)
    return JSONEncoder().encode(result)

@app.route('/', methods=["PUT"])
def update_user():
    userAccess = UserAccess()
    user = json.loads(json.dumps(request.json, cls=DateTimeEncoder), object_hook=User)
    result = userAccess.UpdateUser(user)
    return JSONEncoder().encode(result)

@app.route('/<id>', methods=["DELETE"])
def delete_user(id):
    userAccess = UserAccess()
    user = userAccess.DeleteUser(id)
    return JSONEncoder().encode(user)

@app.route("/user/", methods = ['POST', 'GET'])
def hello():
    userAccess = UserAccess();
    if request.method == 'POST':
        result = request.form
        newUser = User()

        for key, value in result.items():
            if key == "txtname":
                newUser.username = value
            elif key == "txtpass":
                newUser.password = value
            elif key == "txtemail":
                newUser.email = value
        userAccess.InsertUser(newUser);   

    users = userAccess.GetUsers();
    return render_template(
        "index.html",
        users = users
    )

    #git test