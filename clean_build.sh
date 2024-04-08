#!/bin/bash

# Bring down any running containers managed by docker-compose
docker-compose down

# Force remove all containers
docker rm -f $(docker ps -a -q)

# Remove all volumes
docker volume rm $(docker volume ls -q)

# Start up the containers in the background as per docker-compose configuration
docker-compose up