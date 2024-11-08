Project: Deploying a Web Application with Docker and Docker Compose
Overview
In this project, you’ll create a Dockerized environment for a simple web application with a database,
 using Docker Compose to manage services and ensure data persistence.You’ll also use multi-stage builds to optimize the application image.

Project Steps:
Set Up a Simple Web App and Database with Docker Compose

1. Docker Compose: Create a docker-compose.yml file to define multiple services—such as a web application
 (like a simple Node.js app or Python Flask API) and a database (e.g., PostgreSQL or MySQL).

What is Docker Compose?
 Docker Compose is a tool for defining and running multi-container Docker applications.
 It uses a docker-compose.yml file to set up and manage interconnected services.

Example docker-compose.yml:

yaml
Copy code

version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_USER: example_user
      POSTGRES_PASSWORD: example_password
    volumes:
      - db_data:/var/lib/postgresql/data
volumes:
  db_data:


2. Data Persistence in Docker

Explanation: In Docker, data stored in containers is usually temporary.
 By using volumes, you can persist data even if the container stops or restarts.

Example: In the docker-compose.yml file, we defined a db_data volume for the database.
 This means that the PostgreSQL database files will persist outside the container, so data remains even if the container is recreated.

3. Use docker exec to Interact with a Running Container

Explanation: The docker exec command allows you to execute commands inside a running container.
 It’s useful for debugging, testing, and managing containerized applications.

Example Command:

bash
Copy code

docker exec -it <container_name> psql -U example_user -d postgres

This command opens an interactive terminal session in the running db container,
 where you can interact with the PostgreSQL database directly.

4. Multi-Stage Build for the Web Application

Explanation: A multi-stage build in Docker lets you use multiple FROM statements in a Dockerfile to optimize the final image size.
 This is useful for separating build dependencies from the final runtime environment.

Example Dockerfile for Multi-Stage Build:

dockerfile
Copy code

# Stage 1: Build
FROM node:16 as build
WORKDIR /app
COPY . .
RUN npm install && npm run build

# Stage 2: Production
FROM node:16-alpine
WORKDIR /app
COPY --from=build /app/dist /app
EXPOSE 5000
CMD ["node", "app.js"]

Here, the first stage (build) compiles the application, 
while the second stage copies only the necessary files into a smaller, final image.
