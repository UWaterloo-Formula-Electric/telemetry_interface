from app.config import TCP_HOST, TCP_PORT
from app.log.logger import SignalLogger
import threading

if __name__ == '__main__':
    reader = SignalLogger(TCP_HOST, int(TCP_PORT))

    # run reader in thread pool
    thread = threading.Thread(target=reader.start)
    thread.start()
    thread.join()



