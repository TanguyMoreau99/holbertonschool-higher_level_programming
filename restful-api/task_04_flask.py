#!/usr/bin/env python3
"""
This script sets up a simple API using Flask.
It includes endpoints to:
- Return a welcome message at the root URL.
- Provide a list of all usernames.
- Check the API status.
- Return API information.
- Get user data for a specific username.
- Add a new user via a POST request.
"""

# Importing Flask and necessary functions
from flask import Flask, jsonify, request

# Creating the Flask application instance
app = Flask(__name__)

# In-memory data store for users
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


# Route for the root URL, returning a welcome message
@app.route("/")
def home():
    # Return a welcome message
    return "Welcome to the Flask API!"


# Route to get all usernames
@app.route("/data")
def get_data():
    # Return a list of all usernames
    return jsonify(list(users.keys()))


# Route to check the API status
@app.route("/status")
def status():
    # Return OK status
    return "OK"


@app.route('/info')
def get_info():
    # Return API version and description
    return jsonify({
        "version": "1.0",
        "description": "A simple API built with Flask"
    })


# Route to get user data for a specific username
@app.route("/users/<username>")
def get_user(username):
    # Find user data for the given username
    user = users.get(username)
    # If user exists, return the user data
    if user:
        return jsonify(user)
    # If user does not exist, return an error message & 404 status code
    else:
        return jsonify({"error": "User not found"}), 404


# Route to add a new user, accepts POST requests only
@app.route("/add_user", methods=["POST"])
def add_user():
    # Parse the incoming JSON data
    user_data = request.get_json()
    # Check if the JSON data contains the username key
    if "username" not in user_data:
        return jsonify({"error": "Username not provided"}), 400
    username = user_data["username"]
    # Check if the username already exists
    if username in users:
        # If user exists, return an error message & 400 status code
        return jsonify({"error": "User already exists"}), 400
    # Check if all required fields are provided
    required_fields = ["name", "age", "city"]
    for field in required_fields:
        if field not in user_data:
            return jsonify({"error": "{}".format(field.capitalize())}), 400
    # Add new user to the users dictionary
    users[username] = {
        "username": username,
        "name": user_data["name"],
        "age": user_data["age"],
        "city": user_data["city"],
    }
    # Return confirmation message with the user data & 201 status code
    return jsonify({"message": "User added", "user": users[username]}), 201

# Route for undefined endpoints
@app.route("/<path:path>")
def undefined_endpoint(path):
    # Return a JSON response with a 404 status code and an error message
    return jsonify({"error": "Endpoint not found"}), 404


# Start the Flask development server
if __name__ == "__main__":
    # Run the application
    app.run()