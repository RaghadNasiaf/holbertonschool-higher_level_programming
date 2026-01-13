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
    """Retrieves full details for a specific user by their username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user. 
    Includes a check to prevent duplicate usernames (solving the FAIL error).
    """
    data = request.get_json()
    
    # 1. Extract and check if username exists in the request
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # 2. Check for duplicate username (The critical fix for Task 4)
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    # 3. Add the user to the dictionary
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    # Run the Flask development server
    app.run(host='0.0.0.0', port=5000)
