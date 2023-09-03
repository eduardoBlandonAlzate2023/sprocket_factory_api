# Sprocket factory API

An API built using Flask that provides services for sprocket factory data and sprockets.

## Prerequisites

1. Docker
2. Docker Compose

## Instructions

1. Clone the Repository

2. Navigate to the root directory of this repository, where the docker-compose.yml file is located, and run:

- docker-compose build
- docker-compose up api

This will build the image for the application and start the service. Once started, the API will be accessible at:

http://localhost:5000/


3. To run tests, run: docker-compose up test

4. To stop the services, use: docker-compose down

## Endpoints:

Get all factory data: GET http://localhost:5000/factories
Get factory data by ID: GET http://localhost:5000/factories/<FACTORY_ID>
Get sprocket data by ID: GET http://localhost:5000/sprockets/<SPROCKET_ID>
Create a new sprocket: POST http://localhost:5000/sprockets
Update a sprocket by ID: PUT http://localhost:5000/sprockets/<SPROCKET_ID>
