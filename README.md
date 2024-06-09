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

##### Pre-requisites

- Ensure you have Docker and Docker Compose working on your machine
- Clone the repository
- Double check the configurations in `/monitor/app/config.py` (Mainly the TCP host and IP, but you shouldn't need to change it)

##### Use

- In the root folder of the repository, run `./scripts/start_dashboards.sh` in your terminal
- You have two options:

  1. viewing the predefined Grafana dashboard
  2. selecting and viewing graphs of signals you choose in InfluxDB

- For Grafana go to `localhost:3000`
- For InfluxDB go to `localhost:8086`
- When prompted for a login, just enter `uwfe` for username and `uwfepassword` for the password
- When you are finished, hit Ctrl+C and run `./scripts/end.sh` in your terminal

##### Grafana

- After logging in on Grafana, click on `Dashboards` on the left and select `UWFE - General` (or whichever dashboard you would like to see if multiple have been created at the time you are reading this)
- Side note: Changes you make to the dashboard will not be saved after you exit the session, you need to copy the JSON output and paste it into the correct file under `grafana/provisioning/dashboards` if you want the updated dashboard to be generated the next time. Open up a PR if you want to update the dashboard for everyone.

##### InfluxDB

- After logging into InfluxDB, click on `Data Explorer` on the left side. Here you can look up individual signals and their time-series graph. You can filter by either the CAN message (default), by the signal name, or by the sender of the message
- Side note: You will need to periodically hit submit, it doesn't auto-refresh like Grafana does

#### Replaying Logs

Steps

1. Put the log file in /data
2. Edit `config.py` to have LOG_PATH be the path to the file you want to read
3. Uncomment / comment the right function in main.py (there is comments there explaining)
4. Maybe increase line 105 in monitor.py to speed up log replay speed
