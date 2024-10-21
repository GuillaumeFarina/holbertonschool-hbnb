from app.models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, rating, comment, user_id, place_id):
        super().__init__()
        self.rating = self.validate_rating(rating)
        self.comment = comment
        self.user_id = user_id
        self.place_id = place_id

    @staticmethod
    def validate_rating(rating):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        return rating

    @staticmethod
    def add_review(rating, comment, user_id, place_id):
        return Review(rating, comment, user_id, place_id)

    def update_review(self, rating=None, comment=None):
        if rating is not None:
            self.rating = self.validate_rating(rating)
        if comment:
            self.comment = comment
        self.save()
        print(f"Review {self.id} updated successfully")

    def delete_review(self):
        print(f"Review {self.id} has been deleted")

    @staticmethod
    def list_by_place(reviews, place_id):
        return [review for review in reviews if review.place_id == place_id]

    def __str__(self):
        return f"Review {self.id}: Rating: {self.rating}, Comment: {self.comment}, Place ID: {self.place_id}, User ID: {self.user_id}"
