from app.models.base_model import BaseModel
from app.models.place import Place
from app.models.user import User


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = self.validate_text(text)
        self.rating = self.rating_check(rating)
        self.place = self.place_check(place)
        self.user = self.user_check(user)

    @staticmethod
    def validate_text(text):
        if not isinstance(text, str) or len(text) < 1:
            raise ValueError("Text must be a non-empty string.")
        return text

    @staticmethod
    def rating_check(rating):
        if not isinstance(rating, (int, float)):
            raise ValueError('Rating must be a number (integer or float).')
        if rating < 1 or rating > 5:
            raise ValueError('Rating must be between 1 and 5.')
        return rating

    @staticmethod
    def place_check(place):
        if not isinstance(place, Place):
            raise ValueError("Place must be an instance of the Place class.")
        return place

    @staticmethod
    def user_check(user):
        if not isinstance(user, User):
            raise ValueError("User must be an instance of the User class.")
        return user