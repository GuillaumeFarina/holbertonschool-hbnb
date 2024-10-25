from app.models.base_model import BaseModel
from app.models.user import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = self.validate_title(title)
        self.description = description
        self.price = self.price_check(price)
        self.latitude = self.latitude_check(latitude)
        self.longitude = self.longitude_check(longitude)
        self.owner = owner
        self.reviews = []
        self.amenities = []

    @staticmethod
    def validate_data(data):
        if 'title' not in data or 'description' not in data or 'price' not in data or 'latitude' not in data or 'longitude' not in data or 'owner' not in data:
            raise ValueError("Missing required fields")

    def validate_title(title):
        if title not in isinstance(title, str) or len(title) > 100 or len(title) < 1:
            raise ValueError("title is to long")
        return title

    @staticmethod
    def price_check(price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError('Price must be a positive number.')
        return price

    @staticmethod
    def latitude_check(latitude):
        if not isinstance(latitude, (int, float)) or not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90.")
        return latitude

    @staticmethod
    def longitude_check(longitude):
        if not isinstance(longitude, (int, float)) or not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180.")
        return longitude

    def add_review(self, review):
        self.reviews.append(review)

    @staticmethod
    def validate_owner(owner):
        if not isinstance(owner, User):
            raise ValueError("Owner must be an instance of User.")
        return owner.id

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner.id,
            'amenities': [amenity.to_dict() for amenity in self.amenities]
        }
