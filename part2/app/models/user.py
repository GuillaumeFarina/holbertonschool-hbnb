from app.models.base_model import BaseModel
import re


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_owner=False, is_admin=False):
        super().__init__()
        self.first_name = self.validate_name(first_name)
        self.last_name = self.validate_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin
        self.is_owner = is_owner
        self.places = []

    @staticmethod
    def validate_data(data):
        if 'first_name' not in data or 'last_name' not in data or 'email' not in data:
            raise ValueError("Missing required fields")

    @staticmethod
    def validate_name(name):
        if not isinstance(name, str) or len(name) > 50 or len(name) < 1:
            raise ValueError("Name must be a string with 1 to 50 characters.")
        return name

    @staticmethod
    def validate_email(email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(regex, email):
            raise ValueError("Email must follow standard email format.")
        return email

    def check_admin_statu(self):
        return self

    def become_owner(self):
        self.is_owner = True

    @classmethod
    def creat_user():
        pass

    @classmethod
    def update_user(self, data, first_name=None, last_name=None, email=None, is_owner=False):
        """Update the user's attributes."""
        if first_name:
            self.first_name = self.validate_name(first_name)
        if last_name:
            self.last_name = self.validate_name(last_name)
        if email:
            self.email = self.validate_email(email)
        if is_owner:
            self.is_owner = self.is_owner(is_owner)
        super().update(data)
        print(f"User {self.first_name} {self.last_name} updated successfully")

    @classmethod
    def delete_user():
        pass

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin,
            'is_owner': self.is_owner
        }
