# Student Survey Microservices App (FastAPI)

This project implements a microservices-based web application for managing student surveys. The backend is developed using FastAPI and deployed as a containerized microservice on Kubernetes, managed via Rancher on AWS EC2. The application also integrates with an AWS RDS MySQL database and supports a complete CI/CD pipeline using Jenkins and GitHub.

## Features

- FastAPI backend with full CRUD operations for student survey data
- RESTful API with automatic OpenAPI/Swagger documentation
- CI/CD pipeline using GitHub, Jenkins, Docker, and Kubernetes
- Deployed on AWS EC2 with Kubernetes managed via Rancher
- Persistent data storage in AWS RDS (MySQL)

## Tech Stack

| Component       | Technology            |
|----------------|------------------------|
| Backend         | Python, FastAPI        |
| Database        | AWS RDS (MySQL)        |
| Containerization| Docker                 |
| Orchestration   | Kubernetes, Rancher    |
| CI/CD Pipeline  | Jenkins, GitHub        |
| Deployment Host | AWS EC2                |

## Project Structure

```
project-root/
│
├── backend/                   # FastAPI backend
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
│
├── infra/k8s/                 # Kubernetes YAMLs
│   ├── backend-deployment.yaml
│   └── backend-service.yaml
│
├── Jenkinsfile
└── README.md
```

## Setup and Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/survey-app-FastAPI-cicd.git
cd survey-app-FastAPI-cicd
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

This will start the FastAPI app at `http://localhost:8000`

## Docker Build and Run

### Build the Docker Image

```bash
docker build -t survey-backend ./backend
```

### Run the Container

```bash
docker run -d -p 8080:8080 survey-backend
```

## Kubernetes Deployment

Apply the manifests using kubectl:

```bash
kubectl apply -f infra/k8s/backend-deployment.yaml
kubectl apply -f infra/k8s/backend-service.yaml
```

Once deployed, access the service via `http://<your-ec2-public-ip>:30080` if configured using NodePort.

## CI/CD Pipeline with Jenkins

- Jenkins is configured to pull code from GitHub on push
- It builds the Docker image and pushes to Docker Hub
- The image is deployed to the Kubernetes cluster using `kubectl`
- Jenkins node is set up with Docker, kubectl, and Rancher CLI

Ensure Jenkins has the following configured:

- GitHub credentials
- Docker installed and running
- Kubeconfig file for cluster access

## API Testing with Postman

You can test the following endpoints once deployed:

- `POST /survey` - Create a new survey entry
- `GET /survey/{id}` - Retrieve a specific survey
- `PUT /survey/{id}` - Update an existing survey
- `DELETE /survey/{id}` - Delete a survey entry

Swagger documentation is available at:  
`http://<backend-ip>:8080/docs`

## Screenshots

Insert screenshots of the following:

- Jenkins build pipeline
- Deployed service in Rancher
- Kubernetes dashboard
- Postman API test results
- Swagger/OpenAPI UI

## Author

Rabib Ayan 

Computer Science, Drexel University  
Email: rabibayan@gmail.com
