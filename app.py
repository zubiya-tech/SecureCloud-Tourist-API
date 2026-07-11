# SecureCloud Tourist API
# Built by Zubiya | Flask + SQLite + AWS EC2

from flask import Flask, jsonify, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sqlite3
import logging
import os

app = Flask(__name__)

# API key is stored in server environment, not written in this file
API_KEY = os.environ.get("API_KEY")

# Save every request to a log file with time
logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Allow max 15 requests per minute from one IP address
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["15 per minute"]
)

# Add security headers to every response automatically
@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    return response

# Open database connection
def connect_db():
    connection = sqlite3.connect("tourist.db")
    connection.row_factory = sqlite3.Row
    return connection

# Check if request has correct API key in header
def check_api_key():
    key = request.headers.get("X-API-Key")
    return key == API_KEY

# Home page
@app.route('/')
def home():
    return render_template("index.html")

# Quick check to see if server is running
@app.route('/health')
def health():
    logging.info(f"Health check from {request.remote_addr}")
    return jsonify({"status": "healthy", "server": "running"})

# Get all tourist spots - requires API key
@app.route('/spots')
def get_spots():
    if not check_api_key():
        logging.warning(f"Unauthorized /spots attempt from {request.remote_addr}")
        return jsonify({"error": "Unauthorized. Send API key in X-API-Key header."}), 401

    logging.info(f"GET /spots from {request.remote_addr}")
    connection = connect_db()
    spots = connection.execute("SELECT * FROM tourist_spots").fetchall()
    connection.close()
    result = [dict(spot) for spot in spots]
    return jsonify({"status": "success", "total_spots": len(result), "data": result})

# Get spots for one city - requires API key
@app.route('/spots/<city>')
def get_city_spots(city):
    if not check_api_key():
        logging.warning(f"Unauthorized /spots/{city} attempt from {request.remote_addr}")
        return jsonify({"error": "Unauthorized. Send API key in X-API-Key header."}), 401

    # Only allow letters - blocks special characters that could be used in attacks
    if not city.replace(" ", "").isalpha():
        return jsonify({"error": "Invalid city name. Only letters allowed."}), 400

    logging.info(f"GET /spots/{city} from {request.remote_addr}")

    # ? placeholder keeps user input separate from SQL - prevents SQL injection
    connection = connect_db()
    spots = connection.execute(
        "SELECT * FROM tourist_spots WHERE city = ?", (city,)
    ).fetchall()
    connection.close()

    result = [dict(spot) for spot in spots]
    if not result:
        return jsonify({"error": f"No spots found for: {city}"}), 404

    return jsonify({"city": city, "total_results": len(result), "data": result})

# Detail page for one destination
@app.route('/spot/<name>')
def get_spot(name):
    # URL uses hyphens so convert back: "Taj-Mahal" becomes "Taj Mahal"
    destination_name = name.replace("-", " ")
    logging.info(f"GET /spot/{destination_name} from {request.remote_addr}")
    connection = connect_db()
    spot = connection.execute(
        "SELECT * FROM tourist_spots WHERE name = ?", (destination_name,)
    ).fetchone()
    connection.close()
    if spot is None:
        return "Destination not found", 404
    return render_template("spot.html", spot=dict(spot))

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
