#!/usr/bin/python3

import uuid
from datetime import datetime
from app.models.base_model import BaseModel
from app.models.place import Place



class Amenity(BaseModel):
    """
    Amenity Class:
    - id (String): Unique identifier for each amenity.
    - name (String): The name of the amenity (e.g., "Wi-Fi", "Parking"). Required, maximum length of 50 characters.
    - description (String): Detailed description of the amenity. Optional.
    - place_id (String): ID of the place to which the amenity belongs.
    - created_at (DateTime): Timestamp when the amenity is created.
    - updated_at (DateTime): Timestamp when the amenity is last updated.
    """
    def __init__(self, name, place, description=""):
        super().__init__()
        self.id = str(uuid.uuid4())
        self.name = self.validate_name(name)
        self.description = description
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
        if 'name' in data:
            self.name = self.validate_name(data['name'])
        if 'description' in data:
            self.description = data['description']
        self.updated_at = datetime.now()
        super().update(data)

    @staticmethod
    def validate_name(name):
        """Validate the name of the amenity."""
        if not isinstance(name, str) or len(name) > 50 or len(name) < 1:
            raise ValueError("Name must be a string with 1 to 50 characters.")
        return name

    @staticmethod
    def validate_place(place):
        """Validate that the place is an instance of the Place class."""
        if not isinstance(place, Place):
            raise ValueError("Place must be an instance of Place.")
        return place.id

    def add_amenity(self):
        """Add an amenity."""
        print(f"Amenity '{self.name}' added successfully.")

    def update_amenity(self, data):
        """Update the amenity attributes based on the provided dictionary."""
        self.update(data)
        print(f"Amenity '{self.name}' updated successfully.")

    def delete_amenity(self):
        """Delete the amenity."""
        print(f"Amenity '{self.name}' has been deleted.")

    @classmethod
    def list(cls):
        """List all amenities."""
        print("Listing all amenities...")
