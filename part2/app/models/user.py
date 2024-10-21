#!/usr/bin/python3

import uuid
import re
from datetime import datetime
from app.models.base_model import BaseModel


class User(BaseModel):
    """
    User Class:
    - id (String): Unique identifier for each user.
    - first_name (String): The first name of the user. Required, maximum length of 50 characters.
    - last_name (String): The last name of the user. Required, maximum length of 50 characters.
    - email (String): The email address of the user. Required, must be unique, and should follow standard email format validation.
    - password (String): The password of the user. Required, must meet complexity requirements.
    - is_admin (Boolean): Indicates whether the user has administrative privileges. Defaults to False.
    - created_at (DateTime): Timestamp when the user is created.
    - updated_at (DateTime): Timestamp when the user is last updated.
    """
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = self.validate_name(first_name)
        self.last_name = self.validate_name(last_name)
        self.email = self.validate_email(email)
        self.password = self.validate_password(password)
        self.is_admin = is_admin
        self.places = []  # list to store related places

    @staticmethod
    def validate_request_data(data):
        if 'first_name' not in data or 'last_name' not in data or 'email' not in data or 'password' not in data:
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

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r"[0-9]", password):
            raise ValueError("Password must contain at least one digit.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValueError("Password must contain at least one special character.")
        return password

    def check_admin_status(self):
        """Check if the user has administrative privileges."""
        return self.is_admin

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        super().save()

    def update(self, data):
        """
        Update the attributes of the object based on the provided dictionary
        """
        super().update(data)

    def login(self, email, password):
        """Check if the provided email and password match the user's credentials."""
        if self.email == email and self.password == password:
            print(f"Login successful for {self.first_name} {self.last_name}")
            return True
        else:
            print("Invalid email or password")
            return False

    @classmethod
    def create_user(cls, first_name, last_name, email, password, is_admin=False):
        """Create a new user instance."""
        return cls(first_name, last_name, email, password, is_admin)

    def update_user(self, first_name=None, last_name=None, email=None, password=None):
        """Update the user's attributes."""
        if first_name:
            self.first_name = self.validate_name(first_name)
        if last_name:
            self.last_name = self.validate_name(last_name)
        if email:
            self.email = self.validate_email(email)
        if password:
            self.password = self.validate_password(password)
        self.save()
        print(f"User {self.first_name} {self.last_name} updated successfully")

    def delete_user(self):
        """Delete the user instance."""
        print(f"User {self.first_name} {self.last_name} has been deleted")
