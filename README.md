# 🚀 Containerized Microservices System (Flask + MongoDB)

This project demonstrates a simple microservices architecture using Docker and Docker Compose.

It consists of a Flask-based backend API and a MongoDB database running as separate containers, communicating over a shared Docker network.

---

## 🧱 Architecture

* Backend Service → Flask API (Python)
* Database Service → MongoDB
* Containerization → Docker
* Orchestration → Docker Compose
* Data Persistence → Docker Volumes

---

## ⚙️ Features

* REST API with multiple endpoints
* MongoDB integration using PyMongo
* Fully containerized backend
* Multi-container setup using Docker Compose
* Persistent database storage using volumes
* Environment-based configuration (no hardcoded DB URLs)

---

## 📂 Project Structure

```
devops-microservices-project/

├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

## 🔌 API Endpoints

### GET `/`

Returns a health check message

### GET `/users`

Fetch all users from MongoDB

### POST `/users`

Create a new user

#### Example Request:

```json
{
  "name": "Jacob",
  "age": 21
}
```

---

## 🐳 How to Run

Make sure Docker is installed and running.

```
docker-compose up --build
```

Then open:
http://localhost:5000/

---

## 🧠 Key Learnings

* How to containerize a backend service using Docker
* How to connect multiple containers using Docker Compose
* Why `localhost` does not work across containers
* How to use service names as hostnames in Docker networks
* How to persist data using Docker volumes
* How to manage environment variables in containerized apps

---

## 📌 Future Improvements

* Add authentication (JWT)
* Add frontend service
* Deploy using AWS ECS / Kubernetes
* Add CI/CD pipeline

---

## 👨‍💻 Author

Built as part of a DevOps learning project.
