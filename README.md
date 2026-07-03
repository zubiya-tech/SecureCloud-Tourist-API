# SecureCloud Tourist API

A simple tourist destination search app. You enter a city, it finds tourist spots from a database, and shows the details.

Built with Flask + SQLite, deployed on an AWS EC2 server.

Live: http://54.242.127.95:5000

## Why I Built This

Before this I mostly worked with frontend and small scripts. I wanted to understand what's actually happening behind the screen — how a database connects to an API, how something runs on a real server instead of localhost, how you add security to a thing people can hit from the internet.

So I built this to learn those things by doing them, not watching a tutorial about them.

First backend + cloud deployment project I've done. Learned Flask, SQLite, Linux, EC2, Git, and basic API security along the way mostly by breaking things and fixing them.

## What It Does

- Search tourist destinations by city
- Filter by category
- Open a detail page for each destination
- JSON API behind all of it if you want raw data

## Supported Cities

Agra — Taj Mahal, Agra Fort
Delhi — Red Fort, India Gate, Qutub Minar
Mumbai — Gateway of India
Kashmir — Dal Lake
Jaipur — Hawa Mahal, Amer Fort
Hyderabad — Charminar, Golconda Fort
Mysore — Mysore Palace
Amritsar — Golden Temple
Aurangabad — Ajanta Caves, Ellora Caves
Konark — Konark Sun Temple
Madurai — Meenakshi Temple
Chennai — Marina Beach
Goa — Baga Beach
Manali — Manali Hills
Leh — Leh Palace, Pangong Lake
Ooty — Ooty Lake
Munnar — Munnar Tea Gardens
Puri — Jagannath Temple

## Screenshots

### Homepage



![Homepage](screenshots/home-page.png)



### Search Results



![Search Results](screenshots/search-results.png)



### Destination Details



![Destination Details](screenshots/destination-page.png)



## How It Works

\```text
User Browser
      |
      v
Flask Application (AWS EC2)
      |
      v
SQLite Database
\```

Runs on Amazon Linux as a systemd service, so it starts back up on its own after a reboot or a crash. I don't have to SSH in and restart it by hand.

## Security I Added

Data endpoints need an API key. No key, no data.

\```
curl http://54.242.127.95:5000/spots
\```

Response:

\```json
{
  "error": "Unauthorized"
}
\```

### Unauthorized Request



![Unauthorized Request](screenshots/unauthorized-access.png)



### API Request Logs



![API Logs](screenshots/api-log.png)



Past that rate limiting at 100 requests/min per IP, input validation before anything touches the DB, parameterized queries everywhere so there's no string-concatenated SQL, and the basic security headers (X-Frame-Options, X-Content-Type-Options). Requests get logged with timestamp, request info, and IP.

The API key used to be hardcoded in app.py. Bad idea, I know that now moved it to an environment variable plus the systemd config once I understood why that mattered.

Frontend-side auth is still weak. Haven't gotten to fixing that yet.

## API Endpoints

| Endpoint | Authentication |
|----------|----------------|
| / | No |
| /health | No |
| /spots | Yes |
| /spots/<city> | Yes |
| /spot/<name> | No |

## Tech Stack

Python, Flask, SQLite, HTML, CSS, JavaScript, AWS EC2, systemd, Git.

## Project Structure

\```
SecureCloud-Tourist-API/
├── app.py
├── requirements.txt
├── static/
│   ├── script.js
│   └── style.css
└── templates/
    ├── index.html
    └── spot.html
\```

## Run It Yourself

\```
git clone https://github.com/zubiya-tech/SecureCloud-Tourist-API.git
cd SecureCloud-Tourist-API
pip install -r requirements.txt
python app.py
\```

## Problems I Faced

This wasn't just writing routes and calling it done. Real stuff came up along the way the Flask app stopping the second I closed my SSH session, port conflicts from processes I forgot were still running, a git merge conflict I had no idea how to untangle the first time, database files getting tracked by git when they shouldn't have been, and a stretch of just staring at auth errors trying to figure out why the key wasn't matching.

None of that's in a tutorial. You just hit it and figure it out and honestly that taught me more than the tutorials did.

## Limitations

This is a learning project, not a production system. HTTP instead of HTTPS, SQLite instead of something built for real traffic, basic auth, limited destinations.

## Future Improvements

HTTPS, better authentication, move to PostgreSQL, pagination, more destinations.

## What I Learned

Building something is more than writing code. This project took me through the whole path code, server, deployment, security, debugging and most of what I actually learned came from breaking things and having to fix them, not from following steps.

---

Built by **Zubiya** | B.Sc. Computer Science