#!/usr/bin/python3

import uuid
from app.persistence.repository import SQLAlchemyRepository
from datetime import datetime
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from ..models.review import Review

class HBnBFacade:
    def __init__(self):
        # Initialize repositories for users, places, reviews, and amenities
        self.user_repo = SQLAlchemyRepository(User)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)
        self.amenity_repo = SQLAlchemyRepository(Amenity)
        self.users = []
        self.places = []
        self.reviews = []

    """ USER """

    def create_user(self, user_data):
        # Placeholder method for creating a user
        user = User(**user_data)
        # Validate user data
        User.validate_request_data(user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        # Retrieve a user by ID
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

    """ AMENITY """

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

    """ PLACE """

    def create_place(self, place_data):
        # Data Validation
        if not place_data.get('title'):
            raise ValueError('Title is required')
        if not place_data.get('description'):
            raise ValueError('Description is required')
        if not isinstance(place_data.get('price'), (int, float)) or place_data['price'] <= 0:
            raise ValueError('Price must be a positive number')
        if not -90 <= place_data.get('latitude', 0) <= 90:
            raise ValueError('Latitude must be between -90 and 90')
        if not -180 <= place_data.get('longitude', 0) <= 180:
            raise ValueError('Longitude must be between -180 and 180')

        # Create place
        new_place = Place(
            title=place_data['title'],
            description=place_data['description'],
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            owner_id=place_data.get('owner_id'),
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
        # Retrieve place data by ID
        place = self.get_place(place_id)
        if place:
            return place.to_dict()
        else:
            return {'error': 'Place not found'}

    """ REVIEW """

    def create_review(self, review_data):
        # Validate the review data
        Review.validate_request_data(review_data)
        
        # Create a new review with a unique ID
        review = Review(id=str(uuid.uuid4()), **review_data)
        
        # Add the review to the repository
        self.review_repo.add(review)
        print(f"Review added: {review.to_dict()}")
        
        return review

    def get_review(self, review_id):
        # Retrieve a review by its ID
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        # Retrieve all reviews
        return list(self.review_repo.get_all())

    def get_reviews_by_place(self, place_id):
        # Retrieve all reviews for a specific place
        all_reviews = self.review_repo.get_all()
        print(f"Total reviews: {len(all_reviews)}")
    
        # Check that each review has a place_id.
        for review in all_reviews:
            print(f"Review ID: {review.id}, Place ID: {review.place_id}")
    
        filtered_reviews = [review for review in all_reviews if review.place_id == place_id]
        print(f"Filtered reviews for place_id {place_id}: {len(filtered_reviews)}")
    
        return filtered_reviews
    
    def update_review(self, review_id, review_data):
        # Validate the review data
        Review.validate_request_data(review_data)
        
        # Retrieve the existing review
        review = self.get_review(review_id)
        
        if review:
            # Update the review with the new data
            review.update(review_data)
        
        return review

    def delete_review(self, review_id):
        # Delete a review by its ID
        return self.review_repo.delete(review_id)
    
    def add(self, review):
        # Add a review to the list of reviews
        self.reviews.append(review)

    def get(self, review_id):
        # Retrieve a review by its ID
        for review in self.reviews:
            if review.id == review_id:
                return review
        return None

    def get_all(self):
        # Retrieve all reviews
        return self.reviews

    def delete(self, review_id):
        # Delete a review by its ID
        self.reviews = [review for review in self.reviews if review.id != review_id]