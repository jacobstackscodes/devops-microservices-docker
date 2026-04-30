# 🚀 Containerized Microservices System with CI/CD (Flask + MongoDB + Jenkins)

This project demonstrates a complete DevOps workflow by combining containerization and continuous integration/continuous deployment (CI/CD).

It starts with a Dockerized microservices setup (Flask + MongoDB) and extends into an automated pipeline using Jenkins to build and deploy the application.

---

## 🧱 Architecture

### Application Layer

* Backend Service → Flask API (Python)
* Database Service → MongoDB

### DevOps Layer

* Containerization → Docker
* Orchestration → Docker Compose
* CI/CD → Jenkins (running inside Docker)

---

## ⚙️ Features

### Application

* REST API with multiple endpoints
* MongoDB integration using PyMongo
* Environment-based configuration (no hardcoded DB URLs)

### DevOps

* Fully containerized multi-service application
* Automated build and deployment using Jenkins
* Docker socket integration for Jenkins-based deployments
* Persistent database storage using Docker volumes

---

## 🔄 CI/CD Pipeline (Jenkins)

The pipeline automates the deployment process:

1. Jenkins pulls the latest code from GitHub
2. Stops running containers
3. Rebuilds Docker images
4. Deploys updated containers using Docker Compose

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
devops-microservices-docker/

├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── Jenkinsfile
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

## 🐳 How to Run (Local Setup)

Make sure Docker is installed and running.

```
docker-compose up --build
```

Then open:
http://localhost:5000/

---

## ⚙️ How CI/CD Works

* Jenkins runs inside a Docker container
* Docker socket is mounted to Jenkins
* Jenkins executes Docker commands directly
* Pipeline rebuilds and redeploys services automatically

---

## 🧠 Key Learnings

* Containerizing applications using Docker
* Managing multi-container systems with Docker Compose
* Understanding container networking and service communication
* Implementing CI/CD pipelines using Jenkins
* Running Docker commands inside Jenkins containers
* Debugging real-world DevOps issues (permissions, networking, tooling)

---

## 📌 Future Improvements

* Add automated testing stage in pipeline
* Trigger builds using GitHub webhooks
* Create custom Jenkins Docker image (with Docker & Compose preinstalled)
* Deploy using Kubernetes

---

## 👨‍💻 Author

Built as a hands-on DevOps project to demonstrate containerization and CI/CD pipeline implementation.
