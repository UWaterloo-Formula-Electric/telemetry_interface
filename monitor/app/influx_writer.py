import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

from config import INFLUX_URL, INFLUX_BUCKET, INFLUX_TOKEN, INFLUX_ORG

token = INFLUX_TOKEN
org = INFLUX_ORG
url = INFLUX_URL
bucket = INFLUX_BUCKET

write_client = InfluxDBClient(url=url, token=token, org=org)
write_api = write_client.write_api(write_options=SYNCHRONOUS)

def mock_write():
    for value in range(1000):
        point = (
          Point("measurement1")
          .tag("tagname1", "tagvalue1")
          .field("field1", value)
        )
        write_api.write(bucket=bucket, org=INFLUX_ORG, record=point)
        print('wrote: ', value)
        time.sleep(1) # separate points by 1 second