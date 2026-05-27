# SecureCloud Tourist API
# Beginner Backend Project
# Built by Zubiya

from flask import Flask, jsonify

# Create Flask app
app = Flask(__name__)

# Simple tourist data
tourist_spots = [
    {
        "id": 1,
        "name": "Gateway of India",
        "city": "Mumbai",
        "category": "Monument"
    },
    {
        "id": 2,
        "name": "Taj Mahal",
        "city": "Agra",
        "category": "Monument"
    },
    {
        "id": 3,
        "name": "Dal Lake",
        "city": "Kashmir",
        "category": "Nature"
    }
]

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to SecureCloud Tourist API"
    })

# Get all tourist spots
@app.route('/spots')
def get_spots():

    return jsonify({
        "status": "success",
        "total_spots": len(tourist_spots),
        "data": tourist_spots
    })

# Get tourist spots by city
@app.route('/spots/<city>')
def get_city_spots(city):

    filtered_spots = []

    for spot in tourist_spots:

        if spot["city"].lower() == city.lower():
            filtered_spots.append(spot)

    return jsonify({
        "city": city,
        "results": filtered_spots
    })

# Health check route
@app.route('/health')
def health():

    return jsonify({
        "status": "healthy",
        "server": "running"
    })

# Run the server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
