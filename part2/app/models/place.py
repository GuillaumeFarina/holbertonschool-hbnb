from base_model import BaseModel
from user import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title.validate_title(title)
        self.description = description
        self.price = price.price_check(price)
        self.latitude = latitude.latitude_check(latitude)
        self.longitude = longitude.longitude_check(longitude)
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

    def price_check(price):
        if price < 0:
            raise ValueError('prince must be positive')
        return price

    def latitude_check(latitude):
        if not (-90 <= latitude >= 90):
            raise ValueError("latitude not correct")
        return latitude

    def longitude_check(longitude):
        if not (-180 <= longitude >= 180):
            raise ValueError("longitude not correct")
        return longitude

    def user_check(user):
        """def add_review(self, review):
        Add a review to the place.
        self.reviews.append(review)"""

    """def add_amenity(self, amenity):
    Add an amenity to the place.
        self.amenities.append(amenity)"""
