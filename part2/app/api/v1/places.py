from flask import Flask, jsonify, request
from app.models.place import Place

app = Flask(__name__)

places = []


@app.route('/api/v1/places', methods=['POST'])
def creat_place():
    data = request.get_json()

    if not data or not all(k in data for k in ('title', 'description', 'price', 'location')):
        return jsonify({"error": "Missing required fields"}), 400

    new_place = Place(data['title'], data['description'],
                      data['price'], data['location'])
    places.append(new_place)

    return jsonify({"message": "Place created successfully"}), 201


@app.route('/api/v1/places', methods=['GET'])
def list_place():
    return jsonify([place.__dict__ for place in places])


if __name__ == '__main__':
    app.run()
