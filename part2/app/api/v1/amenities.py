from flask import Flask, jsonify, request
from app.models.amenity import Amenity

app = Flask(__name__)

amenities = []


@app.route('/api/v1/amenities ', methods=['POST'])
def creat_amenity():
    data = request.get_json()

    if not data or not all(k in data for k in ('name', 'description')):
        return jsonify({"error": "Missing required fields"}), 400

    new_amenity = Amenity(data['name'], data['description'])
    amenities.append(new_amenity)

    return jsonify({"message": "Amenity created successfully"}), 201


@app.route('/api/v1/amenities', methods=['GET'])
def list_amenity():
    return jsonify([amenity.__dict__ for amenity in amenities])


if __name__ == '__main__':
    app.run()
