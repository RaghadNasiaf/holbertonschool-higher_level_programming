from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store user data in memory
users = {}

@app.route('/')
def home():
    """Endpoint for the root URL."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Returns the status of the API."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Returns the full data for a specific user."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the dictionary via a POST request."""
    data = request.get_json()
    username = data.get("username")
    
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
