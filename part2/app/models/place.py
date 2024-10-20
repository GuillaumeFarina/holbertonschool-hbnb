#!/usr/bin/python3

import uuid
from datetime import datetime
from base_model import BaseModel
from user import User


class Place(BaseModel):
    """
    Place Class:
    - id (String): Unique identifier for each place.
    - title (String): The title of the place. Required, maximum length of 100 characters.
    - description (String): Detailed description of the place. Optional.
    - price (Float): The price per night for the place. Must be a positive value.
    - latitude (Float): Latitude coordinate for the place location. Must be within the range of -90.0 to 90.0.
    - longitude (Float): Longitude coordinate for the place location. Must be within the range of -180.0 to 180.0.
    - owner (User): User instance of who owns the place. This should be validated to ensure the owner exists.
    - created_at (DateTime): Timestamp when the place is created.
    - updated_at (DateTime): Timestamp when the place is last updated.
    """
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = self.validate_title(title)
        self.description = description
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner = self.validate_owner(owner)
        self.amenities = []
        self.reviews = []

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    @staticmethod
    def validate_title(title):
        """Validate the title of the place."""
        if not isinstance(title, str) or len(title) > 100 or len(title) < 1:
            raise ValueError("Title must be a string with 1 to 100 characters.")
        return title

    @staticmethod
    def validate_price(price):
        """Validate the price of the place."""
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        return price

    @staticmethod
    def validate_latitude(latitude):
        """Validate the latitude of the place."""
        if not isinstance(latitude, (int, float)) or not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be within the range of -90.0 to 90.0.")
        return latitude

    @staticmethod
    def validate_longitude(longitude):
        """Validate the longitude of the place."""
        if not isinstance(longitude, (int, float)) or not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be within the range of -180.0 to 180.0.")
        return longitude

    @staticmethod
    def validate_owner(owner):
        """
        Validate that the owner is an instance of the User class.

        Args:
            owner: The owner to validate.

        Raises:
            ValueError: If the owner is not an instance of the User class.

        Returns:
            The validated owner if it is an instance of the User class.
        """
        if not isinstance(owner, User):
            raise ValueError("Owner must be an instance of User.")
        return owner

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        super().save()

    def update(self, data):
        """
        Update the attributes of the object based on the provided dictionary
        """
        super().update(data)

    def create(self):
        """Create a new place instance."""
        print(f"Place '{self.title}' created successfully.")

    def delete(self):
        """Delete the place instance."""
        print(f"Place '{self.title}' has been deleted.")

    @classmethod
    def list(cls):
        """List all places."""
        print("Listing all places...")
