from flask import Flask, jsonify, request
from app.models.user import User

app = Flask(__name__)

users = []


@app.route('/api/v1/users', methods=['POST'])
def creat_user():
    data = request.get_json()
    new_user = User(data['first_name'], data['last_name'],
                    data['email'], data['password'])
    users.append(new_user)
    return jsonify({"message": "User created successfully"}), 201

# ajouter des message d'erreur si la creation marche pas


@app.route('/api/v1/users', methods=['GET'])
def list_users():
    return jsonify([str(user) for user in users])


if __name__ == '__main__':
    app.run()
