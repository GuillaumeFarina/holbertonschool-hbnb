import uuid
from datetime import datetime


class Amenity:
    def __init__(self, name, description):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @staticmethod
    def add_review(name, description):
        return Amenity(name, description)

    def update_review(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description
        self.updated_at = datetime.now()
        print(f"Amenity {self.id} updated successfully")

    def delete_amenity(self):
        print(f"Amenity {self.id} has been deleted")

    def __str__(self):
        return f"Amenity {self.id}: {self.name}, Description: {self.description}"
