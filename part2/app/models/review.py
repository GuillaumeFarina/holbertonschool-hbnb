#!/usr/bin/python3

import uuid
from datetime import datetime
from user import User
from place import Place
from app.models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class:
    - id (String): Unique identifier for each review.
    - rating (Float): Rating given to the place, must be between 1 and 5.
    - comment (String): The content of the review. Required.
    - user_id (String): ID of the user who wrote the review.
    - place_id (String): ID of the place being reviewed.
    - created_at (DateTime): Timestamp when the review is created.
    - updated_at (DateTime): Timestamp when the review is last updated.
    """
    def __init__(self, rating, comment, user, place):
        self.id = str(uuid.uuid4())
        self.rating = self.validate_rating(rating)
        self.comment = self.validate_comment(comment)
        self.user_id = self.validate_user(user)
        self.place_id = self.validate_place(place)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
        if 'comment' in data:
            self.comment = self.validate_comment(data['comment'])
        self.updated_at = datetime.now()
        super().update(data)

    @staticmethod
    def validate_rating(rating):
        """Validate the rating of the review."""
        if not isinstance(rating, (int, float)) or not (1 <= rating <= 5):
            raise ValueError("Rating must be a number between 1 and 5.")
        return rating

    @staticmethod
    def validate_comment(comment):
        """Validate the comment of the review."""
        if not isinstance(comment, str) or len(comment) < 1:
            raise ValueError("Comment must be a non-empty string.")
        return comment

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

    def add_review(self):
        """Add a review."""
        print(f"Review '{self.comment}' added successfully.")

    def update_review(self, data):
        """Update the review attributes based on the provided dictionary."""
        if 'rating' in data:
            self.rating = self.validate_rating(data['rating'])
        if 'comment' in data:
            self.comment = self.validate_comment(data['comment'])
        self.updated_at = datetime.now()
        print(f"Review '{self.comment}' updated successfully.")

    def delete_review(self):
        """Delete the review."""
        print(f"Review '{self.comment}' has been deleted.")

    @classmethod
    def list_by_place(cls, place_id):
        """List all reviews for a specific place."""
        print(f"Listing all reviews for place ID: {place_id}")
