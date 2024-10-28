#!/usr/bin/python3


from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from ..models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
# user
    # Placeholder method for creating a user

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return (user)

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if not user:
            raise ValueError("user not foud")

        if 'first_name' in user_data:
            user.first_name = user_data['first_name']
        if 'last_name' in user_data:
            user.last_name = user_data['last_name']
        if 'email' in user_data:
            user.email = user_data['email']

        self.user_repo.update(user.id, {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })
        return user
    # Placeholder method for fetching a place by ID

    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    # Amenity

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity_by_name(self, amenity_name):
        return self.amenity_repo.get_by_attribute('name', amenity_name)

    def get_amenity_by_id(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity_by_name(amenity_id)
        if not amenity:
            raise ValueError("amenity not foud")

        if 'name' in amenity_data:
            amenity.name = amenity_data['name']

        self.amenity_repo.update(amenity.id, {
            'name': amenity.name,
        })
        return amenity

    # Plac
    def get_place_by_title_and_location(self, title, latitude, longitude):
        for place in self.place_repo.get_all():
            if place.title == title and place.latitude == latitude and place.longitude == longitude:
                return place

    def create_place(self, place_data):
        owner_id = place_data.pop('owner_id')
        owner = self.get_user(owner_id)
        place_data['owner'] = owner
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)

        if 'title' in place_data:
            place.title = place_data['title']
        if 'description' in place_data:
            place.description = place_data['description']
        if 'price' in place_data:
            place.price = place_data['price']

        self.place_repo.update(place.id, {
            'title': place.title,
            'description': place.description,
            'price': place.price
        })
        return place

# Reviews

    def create_review(self, review_data):
        user_id = review_data.pop('user_id')
        user = self.get_user(user_id)
        review_data['user'] = user

        place_id = review_data.pop('place_id')
        place = self.get_place(place_id)
        review_data['place'] = place

        review = Review(**review_data)
        self.review_repo.add(review)

        review.user_id = user_id
        review.place_id = place_id
        print(f"print new revi from facade {review}")
        return review

    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        return review

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        pass

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)


facade = HBnBFacade()
