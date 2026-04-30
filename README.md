# Containerized Microservices Project

This project demonstrates a simple microservices setup using Docker and Docker Compose.

## Tech Stack
- Python (Flask)
- MongoDB
- Docker
- Docker Compose

## Features
- REST API with GET and POST endpoints
- MongoDB integration
- Containerized backend service
- Multi-container setup using Docker Compose
- Persistent database using Docker volumes

## Endpoints

### GET /
Returns a simple message

### GET /users
Fetch all users from MongoDB

### POST /users
Add a new user

## How to Run

```bash
docker-compose up --build