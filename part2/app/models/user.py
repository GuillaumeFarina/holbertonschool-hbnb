from base_model import BaseModel
import re


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = self.validate_name(first_name)
        self.last_name = self.validate_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin
        self.places = []

# valid user_name
    @staticmethod
    def validate_name(name):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 50:
            raise ValueError("Name must be a string with 1 to 50 characters.")
        return name

# valide email format
    @staticmethod
    def validate_email(email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(regex, email):
            raise ValueError("Email must follow standard email format.")
        return email

    def add_(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
