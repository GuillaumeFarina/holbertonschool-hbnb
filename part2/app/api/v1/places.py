#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('places', description='Place operations')

# Define models for associated entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=False, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=False, description="List of amenities ID's"),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

facade = HBnBFacade()

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        place_data = api.payload

        # Validation explicite des données
        if not place_data.get('title'):
            return {'error': 'Title is required'}, 400
        if not isinstance(place_data.get('price'), (int, float)) or place_data['price'] <= 0:
            return {'error': 'Price must be a positive number'}, 400
        if not -90 <= place_data.get('latitude', 0) <= 90:
            return {'error': 'Latitude must be between -90 and 90'}, 400
        if not -180 <= place_data.get('longitude', 0) <= 180:
            return {'error': 'Longitude must be between -180 and 180'}, 400

        try:
            new_place = facade.create_place(place_data)
            return new_place.to_dict(), 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return [place.to_dict() for place in places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        try:
            place = facade.get_place(place_id)
            return place.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 404

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        try:
            place_data = api.payload
            updated_place = facade.update_place(place_id, place_data)
            return updated_place.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 400
