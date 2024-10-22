from base_model import BaseModel
from place import Place


class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = self.validate_name(name)

    @staticmethod
    def validate_name(name):
        if not isinstance(name, str) or len(name) > 50 or len(name) < 1:
            raise ValueError("Name must be a string with 1 to 50 characters.")
        return name
