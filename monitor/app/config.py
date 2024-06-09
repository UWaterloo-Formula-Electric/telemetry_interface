"""
Common application variables
"""

import os

# Core
TCP_HOST = "208.68.36.87"
TCP_PORT = 2333

# DBC
DBC_PATH_OLD = './data/dbc/2018CAR.dbc'
DBC_PATH_NEW = './data/dbc/2024CAR.dbc'

# Dummy Logs
LOG_PATH = './data/Reid_AMS_Fault_3rdRun.log' 

# InfluxDB
INFLUX_URL = "http://influxdb:8086/"
INFLUX_TOKEN = "secrettoken"
INFLUX_ORG = "uwfe"
INFLUX_BUCKET = "telemetry"