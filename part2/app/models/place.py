import uuid
from datetime import datetime


class Place:
    def __init__(self, title, description, price, location):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.location = location
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.amenities = []
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    def update_place(self, title=None, description=None, price=None, location=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if price:
            self.price = price
        if location:
            self.location = location
        self.updated_at = datetime.now()
        print(f"Place '{self.title}' updated successfully")

    def delete_place(self):
        print(
            f"Place '{self.title}' located at {self.location} has been deleted")

    def __str__(self):
        return f"Place {self.title}, Location: {self.location}, Owner: {self.owner.first_name} {self.owner.last_name}"
