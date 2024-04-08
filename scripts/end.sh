#!/bin/bash

# Bring down any running containers managed by docker-compose
docker-compose down

# Force remove all containers
docker rm -f $(docker ps -a -q)

# Remove all volumes
docker volume rm $(docker volume ls -q)