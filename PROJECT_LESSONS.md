# What I Learned — Project 1

Before this project I had never built a backend application. I did not understand how a database connects to an API or how an application runs on a real server. I learned these things by building the project, facing errors, and fixing them.

## What I Built

SecureCloud Tourist API — a Flask + SQLite tourist destination search application deployed on AWS EC2.

Users can search cities, view destinations, and access API endpoints protected with basic security controls.

## Technical Skills I Learned

### Flask
I learned how to create routes, return JSON responses, handle requests, and structure a backend application.

### SQLite
I learned how to connect Python with a database, write queries, and use parameterized queries to prevent SQL injection.

### Cloud Deployment
I learned how to launch an AWS EC2 instance, connect through SSH, deploy the application, open ports, and keep the application running using systemd.

### Security
I learned:
- API key authentication
- Rate limiting
- Input validation
- Security headers
- Logging
- Environment variables
- SQL injection prevention

## Problems I Actually Faced

The hardest part was understanding how the API, database, and server work together.

I faced:
- Git push and merge problems
- Port conflicts from old Flask processes
- Database files being tracked by Git
- Fixing API authentication issues
- Keeping the app running after closing SSH

## Biggest Achievement

The biggest achievement was deploying a real application on AWS EC2 that is accessible from the internet and can reject unauthorized API requests.

This was the first time I built something that was not just running on my own computer.

## What I Would Improve Next

- Add HTTPS
- Improve authentication
- Add more destinations
- Add pagination
- Improve production deployment
