"""Simple app for testing semantic-release."""


def hello():
    return "Hello, world!"

def greet(name):
    return f"Hello, {name}\!"

def farewell(name):
    return f"Goodbye, {name}\!"

def add(a, b):
    return a + b

def authenticate(user, password):
    """First part: basic auth."""
    return user == "admin" and password == "secret"

def get_user_role(user):
    """Second part: role management."""
    roles = {"admin": "superuser", "guest": "readonly"}
    return roles.get(user, "unknown")
