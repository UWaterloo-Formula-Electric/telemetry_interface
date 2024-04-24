# UWFE Telemetry Interface

The goal of this project is to log and visualize the real-time telemetry data produced by our vehicle.

This project is organized as 3 main components:

1. Python code acting as a TCP client to receive and log the live data
2. A local InfluxDB instance where we will write all time-series data
3. A local Grafana dashboard to visualize all the data

## Set up

#### Requirements

The only requirement is that you have Docker and Docker Compose on your computer (https://docs.docker.com/get-docker/).

#### Instructions

To simplify the set up process, there has been Bash scripts created for your convenience.

All you need to do is:

##### Pre-requisites
- Ensure you have Docker and Docker Compose working on your machine
- Clone the repository
- Double check the configurations in `/monitor/app/config.py` (In particular make sure that you have the correct TCP IP and Port that the telemetry data will be read from, the default in that file shouldn't need to be changed if we are reading from the TCP server running on the Bay Computer)

##### Use
- In the root folder of the repository, run `./scripts/start_dashboards.sh` in your terminal
- Open a web browser of your choice and go to `localhost:3000` to access the Grafana dashboards. Alternatively, you can access `localhost:8086` to view the data for individual signals by looking into InfluxDB directly.
- When prompted for a login, just enter `uwfe` for username and `uwfepassword` for the password
- When you are finished, run `./scripts/end.sh` in your terminal

##### Grafana
- After logging in on Grafana, click on `Dashboards` on the left and select `UWFE - General` (or whichever dashboard you would like to see if multiple have been created at the time you are reading this)
- Side note: Changes you make to the dashboard will not be saved after you exit the session, you need to copy the JSON output and paste it into the correct file under `grafana/provisioning/dashboards` if you want the updated dashboard to be generated the next time. Open up a PR if you want to update the dashboard for everyone.

##### InfluxDB
- After logging into InfluxDB, click on `Data Explorer` on the left side. Here you can look up individual signals and their time-series graph. You can filter by either the CAN message (default), by the signal name, or by the sender of the message
- Side note: You will need to periodically hit submit, it doesn't auto-refresh like Grafana does
