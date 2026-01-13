from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Security Configuration
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Use a strong key in production
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# User Data with Hashed Passwords and Roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Basic Authentication Logic ---

@auth.verify_password
def verify_password(username, password):
    """Verifies basic auth credentials."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

# --- JWT Custom Error Handlers (Required for 401 consistency) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

# --- Endpoints ---

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """Authenticates user and returns a JWT token containing role data."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400
        
    username = data.get("username")
    password = data.get("password")
    
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Embed role in the token payload
        access_token = create_access_token(
            identity=username, 
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Route protected by JWT with Role-Based Access Control."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

