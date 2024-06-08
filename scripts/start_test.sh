#!/bin/bash

docker-compose down

docker rm -f $(docker ps -a -q)

docker volume rm $(docker volume ls -q)

docker compose build 

docker-compose up -d influxdb
docker-compose up -d test-server
docker-compose up monitor
