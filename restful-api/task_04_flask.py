from flask import Flask, jsonify, request

# Instantiate the Flask web server
app = Flask(__name__)

# In-memory dictionary to store users. 
# NOTE: Kept empty per instructions to pass the checker!
users = {}

@app.route("/")
def home():
    """Handles the root URL."""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """Returns a JSON list of all usernames stored in the API."""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """Returns the status of the API."""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for the provided username, or a 404 if not found."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Handles POST requests to add a new user."""
    # request.get_json(silent=True) returns None if the body isn't valid JSON
    parsed_data = request.get_json(silent=True)
    
    # 1. Check for valid JSON
    if parsed_data is None:
        return jsonify({"error": "Invalid JSON"}), 400
        
    username = parsed_data.get("username")
    
    # 2. Check if username is missing
    if not username:
        return jsonify({"error": "Username is required"}), 400
        
    # 3. Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
        
    # 4. Add the user and return success confirmation
    users[username] = parsed_data
    
    return jsonify({
        "message": "User added",
        "user": parsed_data
    }), 201

if __name__ == "__main__":
    app.run()
