

from ..app.config import TCP_HOST, TCP_PORT, DBC_PATH_NEW
from ..app.monitor import Monitor


def test_can_process():
    tester = Monitor(TCP_HOST, TCP_PORT, DBC_PATH_NEW)

    tester.process_can_message("0x18C004010FBC32C132B83200")


# why tf isnt pytest working
test_can_process()