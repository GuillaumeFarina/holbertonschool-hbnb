import uuid
from datetime import datetime


class Review:
    def __init__(self, rating, comment, user_id, place_id):
        self.id = str(uuid.uuid4())
        self.rating = rating
        self.comment = comment
        self.user_id = user_id
        self.place_id = place_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @staticmethod
    def add_review(rating, comment, user_id, place_id):
        return Review(rating, comment, user_id, place_id)

    def update_review(self, rating=None, comment=None):
        if rating:
            self.rating = rating
        if comment:
            self.comment = comment
        self.updated_at = datetime.now()
        print(f"Review {self.id} updated successfully")

    def delete_review(self):
        print(f"Review {self.id} has been deleted")

    @staticmethod
    def list_by_place(reviews, place_id):
        return [review for review in reviews if review.place_id == place_id]

    def __str__(self):
        return f"Review {self.id}: Rating: {self.rating}, Comment: {self.comment}, Place ID: {self.place_id}, User ID: {self.user_id}"
