from flask import Flask
from flask_restx import Api


def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API',
              description='API de l’application HBnB')

    # Espace réservé pour les namespaces de l’API (les points de terminaison seront ajoutés plus tard)
    # Des namespaces supplémentaires pour places, reviews, et amenities seront ajoutés plus tard

    return app
