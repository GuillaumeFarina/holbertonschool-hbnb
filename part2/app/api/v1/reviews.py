from flask import Flask, jsonify, request
from app.models.review import Review

app = Flask(__name__)

reviews = []


@app.route('/api/v1/reviews', methods=['POST'])
def creat_review():
    data = request.get_json()

    if not data or not all(k in data for k in ('rating', 'comment', 'user_id', 'place_id')):
        return jsonify({"error": "Missing required fields"}), 400

    new_review = Review(data['rating'], data['comment'],
                        data['user_id'], data['place_id'])
    reviews.append(new_review)

    return jsonify({"message": "Review created successfully", "review": new_review.__dict__}), 201


@app.route('/api/v1/reviews', methods=['GET'])
def list_reviews():
    return jsonify([review.__dict__ for review in reviews])


if __name__ == '__main__':
    app.run()
