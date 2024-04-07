from config import TCP_HOST, TCP_PORT, LOG_PATH
from monitor import Monitor
from influx_writer import mock_write
import time

if __name__ == '__main__':
    start = Monitor(TCP_HOST, int(TCP_PORT))

    for i in range(15):
        print("HJELLLLLLLO")
        time.sleep(1)
    # start.read_log_csv(LOG_PATH, loops=5)
    mock_write()


