from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route('/')
def home():
    """Welcome message for the root endpoint."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns all usernames in the dictionary."""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Returns the API status."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Retrieves full details for a specific user."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user and prevents duplicates."""
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data["username"]
    if username in users:
        # Match the exact error message required by the checker
        return jsonify({"error": "User already exists"}), 400
    
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
