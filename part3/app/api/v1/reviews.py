#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

# Create a namespace for review operations
api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

# Initialize the facade for handling business logic
facade = HBnBFacade()

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        # Get the review data from the request payload
        review_data = api.payload

        try:
            # Create a new review using the facade
            new_review = facade.create_review(review_data)
        except ValueError as error:
            # Return an error response if the review creation fails
            return {'error': f"Review not created: {str(error)}"}, 400

        # Return the newly created review with a 201 status code
        return new_review.to_dict(), 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        # Get the list of all reviews using the facade
        list_of_reviews = facade.get_all_reviews()
        # Return the list of reviews with a 200 status code
        return [review.to_dict() for review in list_of_reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        # Get the review by ID using the facade
        review = facade.get_review(review_id)
        if not review:
            # Return a 404 error if the review is not found
            return {'error': 'Review not found'}, 404
        # Return the review details with a 200 status code
        return review.to_dict(), 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        # Get the review data from the request payload
        review_data = api.payload

        try:
            # Update the review using the facade
            updated_review = facade.update_review(review_id, review_data)
        except ValueError as error:
            # Return a 400 error if the input data is invalid
            return {'error': 'Invalid input data'}, 400

        if not updated_review:
            # Return a 404 error if the review is not found
            return {'error': 'Review not found'}, 404
        # Return a success message with a 200 status code
        return {"message": "Review updated successfully"}, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        # Get the review by ID using the facade
        review = facade.get_review(review_id)
        if not review:
            # Return a 404 error if the review is not found
            return {'error': 'Review not found'}, 404
        # Delete the review using the facade
        facade.delete_review(review_id)
        # Return a success message with a 200 status code
        return {"message": "Review deleted successfully"}, 200

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        # Get the list of reviews for the place using the facade
        list_of_reviews = facade.get_reviews_by_place(place_id)
        # Return the list of reviews with a 200 status code
        return [review.to_dict() for review in list_of_reviews], 200
