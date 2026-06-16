# SecureCloud Tourist API
# Beginner Backend Project
# Built by Zubiya

from flask import Flask, jsonify, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sqlite3
import logging

# Create Flask application
app = Flask(__name__)

# Secret API key - only people with this can access the API
API_KEY = "zt-8f3k9x2m7q1w4e6r0p5n"

# Setup logging - records every request to api.log file
logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Rate limiter - max 100 requests per minute per user
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per minute"]
)

# Security headers - added to every response automatically
@app.after_request
def add_security_headers(response):
    # Stops browser from guessing file types
    response.headers["X-Content-Type-Options"] = "nosniff"
    # Stops your API being loaded inside another website
    response.headers["X-Frame-Options"] = "DENY"
    return response

# Function to connect to SQLite database
def connect_db():
    connection = sqlite3.connect("tourist.db")
    # Makes results come back as dictionaries
    connection.row_factory = sqlite3.Row
    return connection

# Function to check API key on every request
def check_api_key():
    key = request.headers.get("X-API-Key")
    if key != API_KEY:
        return False
    return True

# Home route - shows the HTML search page
@app.route('/')
def home():
    return render_template("index.html")

# Get ALL tourist spots
@app.route('/spots')
def get_spots():
    connection = connect_db()
    spots = connection.execute("SELECT * FROM tourist_spots").fetchall()
    connection.close()
    result = []
    for spot in spots:
        result.append(dict(spot))
    return jsonify({
        "status": "success",
        "total_spots": len(result),
        "data": result
    })

# Get tourist spots for ONE specific city
@app.route('/spots/<city>')
def get_city_spots(city):
    # Only allow letters and spaces - blocks injection attacks
    if not city.replace(" ", "").isalpha():
        return jsonify({"error": "Invalid city name"}), 400
    connection = connect_db()
    spots = connection.execute(
        "SELECT * FROM tourist_spots WHERE city = ?",
        (city,)
    ).fetchall()
    connection.close()
    result = []
    for spot in spots:
        result.append(dict(spot))
    # if no city found return 404
    if len(result) == 0:
        return jsonify({"error": "City not found"}), 404
    return jsonify({
        "city": city,
        "results": result
    })

# Single destination page - converts Taj-Mahal to Taj Mahal
@app.route('/spot/<name>')
def get_spot(name):
    connection = connect_db()
    # Replace hyphens with spaces for URL friendliness
    destination_name = name.replace("-", " ")
    spot = connection.execute(
        "SELECT * FROM tourist_spots WHERE name = ?",
        (destination_name,)
    ).fetchone()
    connection.close()
    if spot is None:
        return "Destination not found", 404
    return render_template("spot.html", spot=dict(spot))

# Health check - quick way to verify server is running
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "server": "running"
    })

# Start Flask server
if __name__ == "__main__":
    app.run(
        debug=False,
        host="0.0.0.0",
        port=5000
    )
