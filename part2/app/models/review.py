from app.models.base_model import BaseModel
from app.models.place import Place


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = self.validate_text(text)
        self.rating = self.rating_check(rating)
        self.place = self.place_check(place)
        self.user = self.user_check(user)
        self.reviews = []
        self.amenities = []

    @staticmethod
    def validate_text(text):
        if not isinstance(text, str) or len(text) < 1:
            raise ValueError("text  .")
        return text

    def rating_check(rating):
        if not isinstance(rating, (int, float)):
            raise ValueError('Rating must be a number (integer or float).')

        if rating < 1 or rating > 5:
            raise ValueError('Rating must be between 1 and 5.')
        return rating

    """def place_check(place.id)
    "check if place exists"""

    """def user_check(user.id)
    "chek if place exists"""
