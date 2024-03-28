"""
Read on the TCP server for data
"""

import socket
import logging
import json
import time

# Setup logging
logging.basicConfig(level=logging.INFO, filename="messages.log",
                    format='%(asctime)s:%(levelname)s:%(message)s')

class SignalLogger:
    def __init__(self, server_address: str, server_port: int):
        self.server_address: str = server_address
        self.server_port: int = server_port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the server
            s.connect((self.server_address, self.server_port))
            logging.info("Connected to server at %s on port %s", self.server_address, self.server_port)
            
            while True:
                # Receive message from the server
                data = s.recv(1024)
                if not data:
                    # No more data from server, can happen if the server closes the connection
                    logging.info("Disconnected from server")
                    break

                # Assuming the message is in JSON format
                try:
                    message = json.loads(data.decode('utf-8'))
                    logging.info("Received JSON message: %s", message)
                    print(message)
                except json.JSONDecodeError:
                    logging.error("Failed to decode JSON from message: %s", data.decode('utf-8'))
                
                # Sleep for a second to manage timing and avoid spamming
                time.sleep(1)