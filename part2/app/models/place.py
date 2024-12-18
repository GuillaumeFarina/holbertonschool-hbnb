#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
from app.models.base_model import BaseModel
from app.models.user import User

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
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None):
        # Initialize the Place with provided attributes and default values
        self.id = str(uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = amenities if amenities else []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
        return owner.id

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()
        super().save()

    def update(self, data):
        """
        Update the attributes of the object based on the provided dictionary
        """
        if 'title' in data:
            self.title = self.validate_title(data['title'])
        if 'description' in data:
            self.description = data['description']
        if 'price' in data:
            self.price = self.validate_price(data['price'])
        if 'latitude' in data:
            self.latitude = self.validate_latitude(data['latitude'])
        if 'longitude' in data:
            self.longitude = self.validate_longitude(data['longitude'])
        self.updated_at = datetime.now()
        super().update(data)

    def create(self):
        """Create a new place instance."""
        print(f"Place '{self.title}' created successfully.")

    @classmethod
    def list(cls):
        """List all places."""
        print("Listing all places...")

    def to_dict(self):
        """Convert the Place object to a dictionary format"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id,
            'amenities': self.amenities,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
