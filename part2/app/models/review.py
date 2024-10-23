#!/usr/bin/python3

from .base_model import BaseModel
import uuid
from datetime import datetime
from app.models.user import User
from app.models.place import Place

class Review(BaseModel):
    def __init__(self, id, text, rating, place_id, user_id):
        self.id = str(uuid.uuid4())
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()
        super().save()

    def update(self, data):
        """
        Update the attributes of the object based on the provided dictionary
        """
        if 'rating' in data:
            self.rating = self.validate_rating(data['rating'])
        if 'text' in data:
            self.text = self.validate_text(data['text'])
        self.updated_at = datetime.now()
        super().update(data)

    @staticmethod
    def validate_rating(rating):
        """Validate the rating of the review."""
        if not isinstance(rating, (int, float)) or not (1 <= rating <= 5):
            raise ValueError("Rating must be a number between 1 and 5.")
        return rating

    @staticmethod
    def validate_text(text):
        """Validate the text of the review."""
        if not isinstance(text, str) or len(text) < 1:
            raise ValueError("text must be a non-empty string.")
        return text

    @staticmethod
    def validate_user(user):
        """Validate that the user is an instance of the User class."""
        if not isinstance(user, User):
            raise ValueError("User must be an instance of User.")
        return user.id

    @staticmethod
    def validate_place(place):
        """Validate that the place is an instance of the Place class."""
        if not isinstance(place, Place):
            raise ValueError("Place must be an instance of Place.")
        return place.id

    @staticmethod
    def validate_request_data(data: dict):
        if 'text' in data:
            if not isinstance(data['text'], str) or len(data['text']) < 1:
                raise ValueError('Text must not be empty')
        if 'rating' in data:
            if not isinstance(data['rating'], int) or not (1 <= data['rating'] <= 5):
                raise ValueError('Rating must be between 1 and 5')
        if 'place_id' in data:
            if not isinstance(data['place_id'], str) or len(data['place_id']) < 1:
                raise ValueError('Place ID must be a non-empty string')
        if 'user_id' in data:
            if not isinstance(data['user_id'], str) or len(data['user_id']) < 1:
                raise ValueError('User ID must be a non-empty string')
        return data
   
    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'user_id': self.user_id,
            'place_id': self.place_id
        }