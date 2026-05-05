# 🚀 Containerized Microservices System with Reverse Proxy & CI/CD

*(Flask + MongoDB + HAProxy + Jenkins)*

This project demonstrates a production-like DevOps setup by combining containerization, reverse proxy configuration, and CI/CD automation.

It includes:

* A Dockerized microservices application (Flask + MongoDB)
* HAProxy as a reverse proxy with load balancing and HTTPS
* Jenkins pipeline for automated build and deployment

---

## 🧱 Architecture

### Application Layer

* **Backend Service** → Flask API (Python)
* **Database Service** → MongoDB

### Networking Layer

* **Reverse Proxy** → HAProxy

  * Routes incoming traffic to backend containers
  * Performs load balancing
  * Handles SSL termination (HTTPS)

### DevOps Layer

* **Containerization** → Docker
* **Orchestration** → Docker Compose
* **CI/CD** → Jenkins (Docker-based)

---

## 🔁 Request Flow

```
Client (Browser / curl)
        ↓
HAProxy (HTTP / HTTPS)
        ↓
Flask Backend (multiple containers)
        ↓
MongoDB
```

---

## ⚙️ Features

### Application

* REST API with multiple endpoints
* MongoDB integration using PyMongo
* Environment-based configuration

### DevOps

* Multi-container Docker setup
* Reverse proxy using HAProxy
* Load balancing across backend instances
* SSL termination using self-signed certificate
* Automated CI/CD pipeline using Jenkins
* Persistent storage using Docker volumes

---

## 🔄 Reverse Proxy (HAProxy)

HAProxy acts as the entry point for all traffic:

* Routes requests to backend containers
* Distributes load using **round-robin**
* Handles HTTPS and forwards requests internally via HTTP

### Ports

| Service         | Port |
| --------------- | ---- |
| HTTP (HAProxy)  | 9090 |
| HTTPS (HAProxy) | 9443 |

---

## 🔐 SSL Setup

* Self-signed certificate generated using OpenSSL
* Combined into a `.pem` file for HAProxy
* HTTPS traffic is terminated at HAProxy

> Note: Browser will show a "Not Secure" warning due to self-signed certificate

---

## 🔄 CI/CD Pipeline (Jenkins)

The pipeline automates deployment:

1. Pull latest code from repository
2. Stop running containers
3. Rebuild images
4. Deploy updated services

### Jenkinsfile

```groovy
pipeline {
    agent any

    stages {
        stage('Build & Deploy') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up --build -d'
            }
        }
    }
}
```

---

## 📂 Project Structure

```
devops-microservices-project/

├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── haproxy/
│   ├── haproxy.cfg
│   └── haproxy.pem
│
├── docker-compose.yml
├── Jenkinsfile
├── README.md
└── .gitignore
```

---

## 🔌 API Endpoints

### GET `/`

Health check

### GET `/users`

Fetch all users

### POST `/users`

#### Example Request:

```json
{
  "name": "Jacob",
  "age": 21
}
```

---

## 🐳 How to Run

Make sure Docker is running.

```bash
docker-compose up --build --scale backend=2
```

---

## 🌐 Access Application

* HTTP → http://localhost:9090
* HTTPS → https://localhost:9443

> Accept browser warning for HTTPS (self-signed certificate)

---

## 🧪 Testing

```bash
curl http://localhost:9090
curl -k https://localhost:9443
```

---

## 🧠 Key Learnings

* Reverse proxy architecture using HAProxy
* SSL termination and HTTPS handling
* Load balancing across multiple containers
* Docker networking and service discovery
* CI/CD automation using Jenkins
* Debugging real-world issues (ports, DNS, SSL, shell behavior)

---

## 📌 Future Improvements

* Add health checks for backend services
* Use Nginx or Traefik for comparison
* Replace self-signed cert with Let's Encrypt
* Deploy to cloud (AWS / GCP)
* Move to Kubernetes for orchestration

---

## 👨‍💻 Author

Built as a hands-on DevOps project demonstrating reverse proxy, load balancing, and CI/CD in a containerized environment.
