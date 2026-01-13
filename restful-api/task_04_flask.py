from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}

@app.route('/')
def home():
    """Returns a simple welcome message."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Returns the API status."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Retrieves detailed info for a specific user."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user and validates for duplicates."""
    data = request.get_json()
    
    # 1. Validate username presence
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data["username"]
    
    # 2. Validate duplicate username (Crucial for passing the test)
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    # 3. Store user data
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
