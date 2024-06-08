

from ..app.config import TCP_HOST, TCP_PORT, DBC_PATH_NEW
from ..app.monitor import Monitor


def test_can_process():
    tester = Monitor(TCP_HOST, TCP_PORT, DBC_PATH_NEW)

    tester.process_can_message("0000AE25x08010C010000000000000000")


# why tf isnt pytest working
test_can_process()
