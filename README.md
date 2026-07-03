# SecureCloud Tourist API

A simple tourist destination search app.

You enter a city, it finds tourist spots from a database, and shows the details.

Built with Flask + SQLite and deployed on an AWS EC2 server.

Live:
http://54.242.127.95:5000

---

## Why I Built This

Before this project, I mostly worked with frontend and small scripts. I wanted to understand what happens behind the screen.

How does a database connect to an API?  
How does an application run on a real server?  
How do you add security to something people can access from the internet?

So I built this project to learn those things by actually doing them.

This became my first backend + cloud deployment project.

I learned Flask, SQLite, Linux, AWS EC2, Git, and basic API security while building, testing, and fixing real problems.

---

## What It Does

The app allows users to:

- Search tourist destinations by city
- Filter results by category
- Open a detail page for each destination
- Access API responses in JSON format

---

## Supported Cities

Currently added destinations include:

- Agra — Taj Mahal, Agra Fort
- Delhi — Red Fort, India Gate, Qutub Minar
- Mumbai — Gateway of India
- Kashmir — Dal Lake
- Jaipur — Hawa Mahal, Amer Fort
- Hyderabad — Charminar, Golconda Fort
- Mysore — Mysore Palace
- Amritsar — Golden Temple
- Aurangabad — Ajanta Caves, Ellora Caves
- Konark — Konark Sun Temple
- Madurai — Meenakshi Temple
- Chennai — Marina Beach
- Goa — Baga Beach
- Manali — Manali Hills
- Leh — Leh Palace, Pangong Lake
- Ooty — Ooty Lake
- Munnar — Munnar Tea Gardens
- Puri — Jagannath Temple
## Screenshots

### Homepage

![Homepage](screenshots/home-page.png)

### Search Results

![Search Results](screenshots/search-results.png)

### Destination Details

![Destination Details](screenshots/destination-page.png)

---

## How It Works

The flow is:

```
User Browser
      |
      v
Flask Application (AWS EC2)
      |
      v
SQLite Database
```

The application runs on Amazon Linux using systemd.

This allows the app to start automatically after a server reboot and restart if it crashes.

---

## Security I Added

While building this project I added:

### API Key Authentication

Protected endpoints require an API key.

Without the key, the API rejects unauthorized requests.

Example:

```bash
curl http://54.242.127.95:5000/spots
```

Response:

```json
{
 "error": "Unauthorized"
}
```
## Security Demonstration

### Unauthorized Request

The API rejects requests that do not include the required API key.

![Unauthorized Request](screenshots/unauthorized-access.png)

### API Request Logs

The application records incoming requests with timestamps and IP addresses for monitoring and debugging.

![API Logs](screenshots/api-log.png)

---

### Rate Limiting

Limits requests to:

100 requests per minute per IP

This reduces excessive API requests and abuse.

---

### Input Validation

User input is checked before database queries.

This prevents invalid requests from reaching the database.

---

### SQL Injection Protection

I used parameterized SQL queries instead of directly placing user input into SQL commands.

---

### Security Headers

Added:

- X-Frame-Options
- X-Content-Type-Options

---

### Logging

Requests are stored with:

- Timestamp
- Request information
- IP address

---

## API Endpoints

| Endpoint | Authentication |
|---|---|
| / | No |
| /health | No |
| /spots | Yes |
| /spots/<city> | Yes |
| /spot/<name> | No |

---

## Tech Stack

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- AWS EC2
- Linux
- systemd
- Git
- GitHub

---

## Project Structure

```
SecureCloud-Tourist-API

├── app.py
├── requirements.txt
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

## Problems I Faced

This project was not only about writing code.

I had to solve real problems:

- Flask app stopping after closing SSH
- Port conflicts from old processes
- Git push and merge issues
- Database files being tracked by Git
- Debugging API authentication problems

Honestly, these problems taught me more than the tutorials because I had to actually figure out what was happening.
___

## Limitations

This is a learning project, not a production system.

Current limitations:

- HTTP instead of HTTPS
- SQLite instead of a production database
- Basic authentication system
- Limited destinations

---

## Future Improvements

- Add HTTPS
- Improve authentication
- Move to PostgreSQL
- Add pagination
- Add more destinations

---

## What I Learned

The biggest thing I learned is that building an application is more than writing code.


So instead of just watching tutorials, I built this and learned by breaking things and fixing them.

This project helped me understand the complete journey from code → server → real users.

---

Built by Zubiya 