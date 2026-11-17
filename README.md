
# Personal Portfolio Website – Docker Deployment

## Project Overview

This project is a personal portfolio website developed using Python Flask and containerized using Docker.

The application showcases my background, technical skills, DevOps learning journey, and projects. It is packaged as a Docker image and deployed on an AWS EC2 instance.

## Technologies Used

- Python 3.12
- Flask
- Docker
- Docker Hub
- AWS EC2
- Linux
- Git and GitHub

## Project Structure

```text
my-docker-file/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

## Run the Application Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Build the Docker image

```bash
docker build -t my-python-app .
```

### 3. Run the Docker container

```bash
docker run -d --name portfolio-app -p 5000:5000 my-python-app
```

### 4. Access the application

Open this URL in your browser:

```text
http://localhost:5000
```

For an EC2 deployment, use:

```text
http://YOUR_EC2_PUBLIC_IP:5000
```

Make sure inbound TCP port 5000 is allowed in the EC2 Security Group.

## Docker Hub

Docker image: `YOUR_DOCKERHUB_USERNAME/YOUR_IMAGE_NAME:latest`

Pull the image:

```bash
docker pull YOUR_DOCKERHUB_USERNAME/YOUR_IMAGE_NAME:latest
```

Run the image:

```bash
docker run -d --name portfolio-app -p 5000:5000 YOUR_DOCKERHUB_USERNAME/YOUR_IMAGE_NAME:latest
```

## Deployment Workflow

1. Develop the Flask application.
2. Create a Dockerfile.
3. Build the Docker image.
4. Test the container locally.
5. Push the Docker image to Docker Hub.
6. Deploy the container on AWS EC2.
7. Push the project source code and documentation to GitHub.

## Author

**Hajee Syed Aboothahir**

DevOps / Cloud Engineer

GitHub: https://github.com/HajeeAboothahir

---

This project demonstrates the basics of containerizing a Python Flask application, publishing a Docker image, and deploying a containerized application on AWS EC2.
