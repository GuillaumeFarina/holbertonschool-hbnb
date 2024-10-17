import uuid
from datetime import datetime


class User:
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self._email = email
        self._password = password
        self.is_admin = is_admin
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []

    def add_place(self, place):
        self.places.append(place)

    def login(self, email,  password):
        if self._email == email and self._password == password:
            print(f"Login successful for {self.first_name} {self.last_name}")
            return True
        else:
            print("invalide email or password")
            return False

    def create_user(first_name, last_name, email, password, is_admin=False):
        return User(first_name, last_name, email, password, is_admin)

    def update_user(self, first_name=None, last_name=None, email=None, password=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email:
            self._email = email
        if password:
            self._password = password
        self.updated_at = datetime.now()
        print(f"User {self.first_name} {self.last_name} updated successfully")

    def delete_user(self):
        print(f"User {self.first_name} {self.last_name} has been deleted")

    def __str__(self):
        return f"User {self.first_name} {self.last_name}, Email: {self._email}, Admin: {self.is_admin}"
