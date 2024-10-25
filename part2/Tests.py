#!/usr/bin/python3
import unittest
from app import create_app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "John.doe@example.com",
            "password": "Password123@",
        })
        self.assertEqual(response.status_code, 201)

    def test_email_already_use(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Johnny",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "Password123@",
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Email already registered', response.get_json()['error'])

    def test_List_of_users_retrieved_successfully(self):
        response = self.client.get('/api/v1/users/', json={
        "id": "950c0510-bcd2-4451-af76-c5dfb23583d1",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        })
        self.assertEqual(response.status_code, 200)

    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "invalid-email",
            "password": "Password123@"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid email format', response.get_json()['error'])

    def test_create_user_be_a_string(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "jon@hotmail.com",
            "password": "Password123@"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Name must be a string with 1 to 50 characters.', response.get_json()['error'])

    def test_user_not_found(self):
        response = self.client.post('/api/v1/users/{user_id}', json={
            "id": "25a5d7af-",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
        })
        response = self.client.get('/api/v1/users/nonexistent_user_id')
        self.assertEqual(response.status_code, 404)
        json_response = response.get_json()
        if json_response:
            self.assertIn('User not found', json_response['error'])
    
    def test_update_user(self):
    # Créez d'abord un utilisateur
        response = self.client.post('/api/v1/users/', json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "Password123@"
        })
        self.assertEqual(response.status_code, 201)

        # Mettez à jour l'utilisateur créé
        response = self.client.put('/api/v1/users/{user_id}', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "password": "Password123@"
        })
        self.assertEqual(response.status_code, 200)

class TestAmenityEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Wi-fi"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_amenity_invalid_data(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": ""
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid input data', response.get_json()['error'])
    
    def test_get_retrieve_all_amenities(self):
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/api/v1/amenities/{amenity_id}', json={
            "id": "1f97c1f9-c171-",
            "error": "Amenity not found"
            })
        self.assertEqual(response.status_code, 404)
        self.assertIn('Amenity not found', response.get_json()['error'])
    
    def test_update_amenity(self):
        response_amenity = self.client.post('/api/v1/amenities/', json={
            "name": "Wi-Fi"
        })
        amenity_id = response_amenity.get_json()['id']

        response_updated_amenity = self.client.put(f'/api/v1/amenities/{amenity_id}', json={
            "name": "Air Conditioning"
        })
        self.assertEqual(response_updated_amenity.status_code, 200)

class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
    
    def test_create_place(self):
        response = self.client.post('/api/v1/users/', json={
        "title": "Cozy Apartment",
        "description": "A nice place to stay",
        "price": 100.0,
        "latitude": 37.7749,
        "longitude": -122.4194,
        "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        })

        response = self.client.post('/api/v1/places/', json={
        "id": "50df63d4-8649-47db-b2a9-8452e26b0350",
        "title": "Cozy Apartment",
        "description": "A nice place to stay",
        "price": 100,
        "latitude": 37.7749,
        "longitude": -122.4194,
        "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "amenities": [],
        "created_at": "2024-10-25T17:37:20.780809",
        "updated_at": "2024-10-25T17:37:20.780812"
        })

        self.assertEqual(response.status_code, 201)

    def test_create_place_invalid_title(self):
        response = self.client.post('/api/v1/users/', json={
            "title": "",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        response = self.client.post('/api/v1/places/', json={
        "message": "Title is required"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Title is required', response.get_json()['error'])
    
    def test_get_places(self):
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)

    def test_update_place(self):
        response_place = self.client.post('/api/v1/places/', json={
            "title": "Luxury Condo",
            "description": "An upscale place to stay",
            "price": 200.0
        })
        place_id = response_place.get_json()

        response_updated_place = self.client.put(f'/api/v1/places/{place_id}', json={
            "id": "187d28d8-1a4c-4efe-8ad4-b50ea7c5b247",
            "title": "Luxury Condo",
            "description": "An upscale place to stay",
            "price": 200,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "amenities": [],
            "created_at": "2024-10-25T18:12:02.584586",
            "updated_at": "2024-10-25T18:12:25.306277"
        })
        self.assertEqual(response_updated_place.status_code, 200)

    def test_place_not_found(self):
        response_place = self.client.post('/api/v1/places/', json={
            "title": "Luxury Condo",
            "description": "An upscale place to stay",
            "price": 200.0
        })
        place_id = response_place.get_json()['id']

        response_updated_place = self.client.put(f'/api/v1/places/{place_id}', json={
            "message": "Place not found."
        })
        self.assertEqual(response_updated_place.status_code, 400)
        self.assertIn('Place not found.', response_updated_place.get_json()['error'])

class TestReviewEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_review(self):
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Great place",
            "rating": 5,
            "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "place_id": "1fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_review_invalid_data(self):
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Great place to stay!",
            "rating": 0,
            "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "place_id": "1fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Review not created: Rating must be between 1 and 5', response.get_json()['error'])

    def test_get_reviews(self):
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)

    def test_get_reviews_id(self):
        response = self.client.get('/api/v1/reviews/{review_id}', json={
            "error": "Review not found"
        })
        self.assertEqual(response.status_code, 404)
        self.assertIn('Review not found', response.get_json()['error'])

    def test_place_id(self):
        response = self.client.get('/api/v1/reviews/place/{review_id}/reviews', json={
            "id": "17da93ef-9335-47fc-9f38-9e16ccb89754",
            "text": "Great place to stay!",
            "rating": 5,
            "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "place_id": "1fa85f64-5717-4562-b3fc-2c963f66afa6"
        })

        response = self.client.get('/api/v1/reviews/place/{review_id}/reviews', json={
            "id": "17da93ef-9335-47fc-9f38-9e16ccb89754",
            "text": "Great place to stay!",
            "rating": 5,
            "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "place_id": "1fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        self.assertEqual(response.status_code, 200)

    def test_update_review(self):
        response = self.client.put('/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)
    
    def test_delete_review(self):
        response = self.client.delete('/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()