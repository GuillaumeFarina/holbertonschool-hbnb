from app.models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner = owner
        self.reviews = []
        self.amenities = []

    @staticmethod
    def validate_price(price):
        if price <= 0:
            raise ValueError("Price must be positive")
        return price

    @staticmethod
    def validate_latitude(latitude):
        if not -90 <= latitude <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        return latitude

    @staticmethod
    def validate_longitude(longitude):
        if not -180 <= longitude <= 180:
            raise ValueError("Longitude must be between -180 and 180")
        return longitude

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    def update_place(self, title=None, description=None, price=None, latitude=None, longitude=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if price is not None:
            self.price = self.validate_price(price)
        if latitude is not None:
            self.latitude = self.validate_latitude(latitude)
        if longitude is not None:
            self.longitude = self.validate_longitude(longitude)
        self.save()
        print(f"Place '{self.title}' updated successfully")

    def delete_place(self):
        print(
            f"Place '{self.title}' located at {self.location} has been deleted")

    def __str__(self):
        return f"Place {self.title}, Location: ({self.latitude}, {self.longitude}), Owner: {self.owner.first_name} {self.owner.last_name}"
