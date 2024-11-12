from datetime import datetime
import uuid
from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        # Initialize the Amenity with a unique ID and timestamps
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().__init__()
        self.name = name

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()
        super().save()

    def update(self, data):
        """
        Update the attributes of the object based on the provided dictionary
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
        super().update(data)

    @staticmethod
    def validate_request_data(data: dict):
        """
        Validate the request data for creating or updating an Amenity
        """
        for key, value in data.items():
            if key == 'name':
                if not isinstance(value, str) or len(value) < 1 or len(value) > 50:
                    raise ValueError('Name must be a non-empty string with a maximum length of 50 characters')
        return data

    def to_dict(self):
        """
        Convert the Amenity object to a dictionary format
        """
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
