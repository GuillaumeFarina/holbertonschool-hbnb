#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
import re

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'is_owner': fields.Boolean(required=False, description='is_owner of the user')
})

facade = HBnBFacade()

def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(regex, email):
        raise ValueError("Invalid email format")
    return email

class User:
    def __init__(self, id, first_name, last_name, email, password, is_owner=False):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_owner = is_owner

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Validate email format
        try:
            validate_email(user_data['email'])
        except ValueError as e:
            return {'error': str(e)}, 400

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400
        try:
            new_user = facade.create_user(user_data)
        except Exception as e:
            return {"Error": str(e)}, 500
        return new_user.to_dict(), 201

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Retrieve the list of users"""
        users = facade.get_all_users()
        return [user.to_dict() for user in users], 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return user.to_dict(), 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        """Update user information"""
        user_data = api.payload

        # Validate email format
        try:
            validate_email(user_data['email'])
        except ValueError as e:
            return {'error': str(e)}, 400

        updated_user = facade.update_user(user_id, user_data)
        if not updated_user:
            return {'error': 'User not found'}, 404
        return updated_user.to_dict(), 200
