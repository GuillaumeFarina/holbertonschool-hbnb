from flask import Flask
from flask_restx import Api
from .v1.amenities import api as amenities_api

app = Flask(__name__)
api = Api(app)

api.add_namespace(amenities_api, path='/api/v1/amenities')

if __name__ == '__main__':
    app.run(debug=True)
