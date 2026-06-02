# SecureCloud Tourist API
# Beginner Backend Project
# Built by Zubiya

from flask import Flask, jsonify
import sqlite3

# Create Flask application
app = Flask(__name__)

# Function to connect to SQLite database
def connect_db():

    connection = sqlite3.connect("tourist.db")

    # Convert database rows into dictionaries
    connection.row_factory = sqlite3.Row

    return connection


# Home route
@app.route('/')
def home():

    return jsonify({
        "message": "Welcome to SecureCloud Tourist API"
    })


# Get all tourist spots
@app.route('/spots')
def get_spots():

    # Connect to database
    connection = connect_db()

    # Get all tourist spots
    spots = connection.execute(
        "SELECT * FROM tourist_spots"
    ).fetchall()

    # Close database connection
    connection.close()

    # Convert rows to dictionary format
    result = []

    for spot in spots:
        result.append(dict(spot))

    return jsonify({
        "status": "success",
        "total_spots": len(result),
        "data": result
    })


# Get tourist spots by city
@app.route('/spots/<city>')
def get_city_spots(city):

    # Connect to database
    connection = connect_db()

    # Find matching city
    spots = connection.execute(
        "SELECT * FROM tourist_spots WHERE city = ?",
        (city,)
    ).fetchall()

    # Close database connection
    connection.close()

    result = []

    for spot in spots:
        result.append(dict(spot))

    return jsonify({
        "city": city,
        "results": result
    })


# Health check route
@app.route('/health')
def health():

    return jsonify({
        "status": "healthy",
        "server": "running"
    })


# Start Flask server
if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
