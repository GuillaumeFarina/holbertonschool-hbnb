from app.persistence.repository import InMemoryRepository
from ..models.user import User
from ..models.amenity import Amenity
import hashlib


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def hash_password(self, password):
        # Utilisation de hashlib pour hasher le mot de passe
        return hashlib.sha256(password.encode()).hexdigest()

    # USER
    def create_user(self, user_data):
        # Vérifier si l'email existe déjà
        if self.get_user_by_email(user_data['email']):
            raise ValueError("Email already registered")

        # Hasher le mot de passe
        user_data['password'] = self.hash_password(user_data['password'])

        # Créer l'utilisateur
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        user = self.user_repo.get_by_attribute('email', email)
        if user:
            print(f"Utilisateur trouvé: {user.first_name} {user.last_name}")
        else:
            print("Aucun utilisateur trouvé")
        return user

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)
        if not user:
            return None

        # Vérifier les données à mettre à jour
        if 'password' in user_data:
            user_data['password'] = self.hash_password(user_data['password'])

        # Mettre à jour l'utilisateur
        user.update_user(
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
            email=user_data.get('email'),
            password=user_data.get('password')
        )
        return user

    # AMENITY
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        amenity.update_amenity(
            name=amenity_data.get('name'),
            description=amenity_data.get('description')
        )
        return amenity
