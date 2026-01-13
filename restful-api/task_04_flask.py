from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# In-memory dictionary to store user data
users = {}

@app.route('/')
def home():
    """Root endpoint that returns a welcome message."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns a list of all usernames stored in the system."""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Returns the current status of the API."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Retrieves full details for a specific user."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user and validates for duplicates."""
    data = request.get_json()
    
    # 1. Check if username is provided
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # 2. Check for duplicate username (Critical for passing the test)
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    # 3. Store the user data
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    # Run the server on all addresses and port 5000
    app.run(host='0.0.0.0', port=5000)
