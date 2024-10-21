from app.models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description

    @staticmethod
    def add_amenity(name, description):
        return Amenity(name, description)

    def update_amenity(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description
        self.save()
        print(f"Amenity {self.id} updated successfully")

    def delete_amenity(self):
        print(f"Amenity {self.id} has been deleted")

    def __str__(self):
        return f"Amenity {self.id}: {self.name}, Description: {self.description}"
