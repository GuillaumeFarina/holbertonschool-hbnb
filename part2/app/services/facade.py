#!/usr/bin/python3

from uuid import uuid4
from app.persistence.repository import InMemoryRepository
from datetime import datetime
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.places = []

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

        """
    PLACE
    """
    def create_place(self, place_data):
        # Validate the data
        if place_data['price'] < 0:
            raise ValueError("Price must be a non-negative float.")
        if not (-90 <= place_data['latitude'] <= 90):
            raise ValueError("Latitude must be between -90 and 90.")
        if not (-180 <= place_data['longitude'] <= 180):
            raise ValueError("Longitude must be between -180 and 180.")
        
        # Create the place
        new_place = Place(
            title=place_data['title'],
            description=place_data['description'],
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            owner_id=place_data['owner_id'],
            amenities=place_data.get('amenities', [])
        )
        self.places.append(new_place)
        return new_place

    def get_place(self, place_id):
        # Retrieve the place by ID
        for place in self.places:
            if place.id == place_id:
                return place
        raise ValueError("Place not found.")

    def get_all_places(self):
        # Retrieve all places
        return self.places

    def update_place(self, place_id, place_data):
        # Retrieve the place by ID
        place = self.get_place(place_id)
        
        # Update the place data
        if 'title' in place_data:
            place.title = place_data['title']
        if 'description' in place_data:
            place.description = place_data['description']
        if 'price' in place_data:
            place.price = place_data['price']
        if 'latitude' in place_data:
            place.latitude = place_data['latitude']
        if 'longitude' in place_data:
            place.longitude = place_data['longitude']
        if 'amenities' in place_data:
            place.amenities = place_data['amenities']
        place.updated_at = datetime.now()
        return place

    def get_place_data(self, place_id):
        place = self.get_place(place_id)
        if place:
            return place.to_dict()
        else:
            return {'error': 'Place not found'}
