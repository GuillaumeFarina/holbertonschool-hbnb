#!/usr/bin/python3

from app.persistence.repository import InMemoryRepository
from ..models.user import User
from ..models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    """ 
    USER
    """
    def create_user(self, user_data):
        # Placeholder method for creating a user
        user = User(**user_data)
        # User.check(user_data)
        User.validate_request_data(user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        # Placeholder method for fetching a user by ID
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        # Placeholder method for fetching a user by email
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        # Placeholder for logic to retrieve a list of all users
        return list(self.user_repo.get_all())

    def update_user(self, user_id, user_data):
        # Placeholder for logic to update a user
        User.validate_request_data(user_data)
        obj = self.get_user(user_id)
        if obj:
            obj.update(user_data)
        return obj

    """ 
    AMENITY 
    """
    def create_amenity(self, amenity_data):
        # Placeholder for logic to create an amenity
        amenity = Amenity(**amenity_data)
        Amenity.validate_request_data(amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        # Placeholder for logic to retrieve an amenity by ID
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        # Placeholder for logic to retrieve all amenities
        return list(self.amenity_repo.get_all())

    def update_amenity(self, amenity_id, amenity_data):
        # Placeholder for logic to update an amenity
        Amenity.validate_request_data(amenity_data)
        obj = self.get_amenity(amenity_id)
        if obj:
            obj.update(amenity_data)
        return obj
       