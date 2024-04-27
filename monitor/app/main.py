from config import TCP_HOST, TCP_PORT, LOG_PATH, DBC_PATH_OLD, DBC_PATH_NEW
from monitor import Monitor
from influx_writer import mock_write
import time

if __name__ == '__main__':
    start = Monitor(TCP_HOST, TCP_PORT, DBC_PATH_NEW)

    for i in range(3):
        print("Buffer time...")
        time.sleep(1)
        
    start.simulate_random()
    # start.read_tcp()
    # tester = Monitor(TCP_HOST, TCP_PORT, DBC_PATH_NEW)

    # tester.process_can_message("0x18C0040110C432AE32BB3200")



