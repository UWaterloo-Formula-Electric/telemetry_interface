from config import TCP_HOST, TCP_PORT, LOG_PATH, DBC_PATH_OLD, DBC_PATH_NEW
from monitor import Monitor
from influx_writer import mock_write
import time

if __name__ == '__main__':
    start = Monitor(TCP_HOST, TCP_PORT, DBC_PATH_NEW)

    for i in range(3):
        print("Buffer time to allow Influx and Grafana to start up...")
        time.sleep(1)
        
    # start.simulate_random()
    # start.simulate_telemetry(LOG_PATH)
    start.read_tcp()
    # tester = Monitor('host.docker.internal', 12345, DBC_PATH_NEW)
    # tester.read_tcp()
    # tester.process_can_message("0x18C0040110C432AE32BB3200")


