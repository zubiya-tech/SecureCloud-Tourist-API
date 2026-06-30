# SecureCloud Tourist API

A tourist destination search app where users can enter a city name and view tourist destinations. Built with Flask and SQLite, and deployed on AWS EC2.

Live Demo: http://54.242.127.95:5000

---

## Why I Built This

I built this project to learn how backend development works in real life.

I wanted to understand how a database connects to an API, how to deploy an application on a real server, and how security is added to a web application.

This project helped me learn Flask, SQLite, Linux, AWS EC2, Git, and basic API security by building, testing, and debugging a real application.

---

## What It Does

- Search tourist destinations by city name
- Filter results by category
- View a detail page for each destination
- REST API that returns JSON responses

---

## Cities and Destinations

| City | Destinations |
|------|-------------|
| Agra | Taj Mahal, Agra Fort |
| Delhi | Red Fort, India Gate, Qutub Minar |
| Mumbai | Gateway of India |
| Kashmir | Dal Lake |
| Jaipur | Hawa Mahal, Amer Fort |
| Hyderabad | Charminar, Golconda Fort |
| Mysore | Mysore Palace |
| Amritsar | Golden Temple |
| Aurangabad | Ajanta Caves, Ellora Caves |
| Konark | Konark Sun Temple |
| Madurai | Meenakshi Temple |
| Chennai | Marina Beach |
| Goa | Baga Beach |
| Manali | Manali Hills |
| Leh | Leh Palace, Pangong Lake |
| Ooty | Ooty Lake |
| Munnar | Munnar Tea Gardens |
| Puri | Jagannath Temple |

---

## Screenshots

### Homepage

![Homepage](screenshots/home-page.png)

### Search Results

![Search Results](screenshots/search-results.png)

### Destination Page

![Destination Page](screenshots/destination-page.png)

---

## Architecture

```
User Browser
      |
      v
Flask Application (AWS EC2)
      |
      v
SQLite Database
```

Deployment:

- AWS EC2
- Amazon Linux
- systemd service for automatic startup

---

# Security Features

I added these security features while building the project:

## API Key Authentication

The data endpoints are protected using API key authentication.

Without the correct key:

```bash
curl http://54.242.127.95:5000/spots

{"error":"Unauthorized. Send API key in X-API-Key header."}
```

With the key:

```bash
curl http://54.242.127.95:5000/spots/Delhi \
-H "X-API-Key: your-key"
```

---

## Rate Limiting

Maximum 100 requests per minute per IP address.

This helps reduce API abuse and excessive requests.

---

## Input Validation

City names are checked before database queries.

This prevents invalid input and reduces the risk of malicious requests.

---

## Parameterized SQL Queries

User input is never directly inserted into SQL queries.

Parameterized queries are used to prevent SQL injection attacks.

---

## Security Headers

Responses include:

- X-Frame-Options
- X-Content-Type-Options

These provide additional browser security protections.

---

## Request Logging

API requests are stored in log files with:

- Timestamp
- Request information
- IP address

---

## Environment Variables

Sensitive values are managed using environment variables on the backend.

The current frontend authentication approach is a known limitation and can be improved with stronger authentication methods in future projects.

---

# API Endpoints

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| GET | / | No | Search homepage |
| GET | /health | No | Check if server is running |
| GET | /spots | Yes | Get all tourist spots |
| GET | /spots/<city> | Yes | Get spots for one city |
| GET | /spot/<name> | No | Detail page for one destination |

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python + Flask | Backend API |
| SQLite | Database |
| HTML, CSS, JavaScript | Frontend |
| AWS EC2 | Cloud hosting |
| systemd | Keeps application running |
| Git + GitHub | Version control |

---

# Project Structure

```
SecureCloud-Tourist-API/

├── app.py
├── requirements.txt
├── PROJECT_LESSONS.md
│
├── static/
│   ├── script.js
│   └── style.css
│
└── templates/
    ├── index.html
    └── spot.html
```

---

# How to Run Locally

```bash
git clone https://github.com/zubiya-tech/SecureCloud-Tourist-API.git

cd SecureCloud-Tourist-API

pip install -r requirements.txt

python app.py
```

---

# Known Limitations

- The application currently uses HTTP instead of HTTPS, so data is not encrypted in transit.
- SQLite works well for this learning project but is not suitable for high-traffic production systems.
- Authentication can be improved further with sessions, OAuth, or other secure methods.

---

# What I Would Add Next

- HTTPS support
- Better authentication system
- More cities and destinations
- Pagination for larger datasets
- PostgreSQL for production-level database usage

---

# What I Learned

This was my first backend and cloud deployment project.

The hardest part was understanding how the API, database, and server connect together — and testing that the security features actually work, not just writing the code.

I learned that building an application is not only about coding. It is also about deploying, debugging, securing, and maintaining the system.

---

Built by Zubiya
