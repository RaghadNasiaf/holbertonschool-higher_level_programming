from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}

@app.route('/')
def home():
    """Welcome message for the root endpoint."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns a JSON list of all usernames."""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Simple status check endpoint."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Retrieves detailed information for a specific user."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user and validates inputs and duplicates."""
    # Use request.get_json() to parse incoming data
    data = request.get_json()
    
    # Check if data is provided
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
        
    username = data.get("username")
    
    # Requirement: Check if username is missing
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # Requirement: Check for duplicates (The fix for your FAIL)
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    # Store user data
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
