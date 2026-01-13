from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {}

@app.route('/')
def home():
    """Root endpoint welcome message."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns a list of all stored usernames."""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Health check endpoint."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Retrieves specific user details."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user with validation for JSON, presence, and duplicates."""
    # Check for valid JSON
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    
    data = request.get_json()
    
    # Check if username is provided
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data["username"]
    
    # Check for duplicate username (Using 409 Conflict and exact message)
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # Store user data
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

