from config import TCP_HOST, TCP_PORT, LOG_PATH, DBC_PATH
from monitor import Monitor
from influx_writer import mock_write
import time

if __name__ == '__main__':
    start = Monitor(TCP_HOST, TCP_PORT, DBC_PATH)

    for i in range(5):
        print("Buffer time... loading...")
        time.sleep(1)
    start.simulate_telemetry(LOG_PATH)
    # mock_write()


