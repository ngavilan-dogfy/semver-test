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
