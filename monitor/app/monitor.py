"""
Read on the TCP server for data
"""

import socket
import json
import time
from datetime import datetime

class Monitor:
    def __init__(self, server_address: str, server_port: int):
        self.server_address: str = server_address
        self.server_port: int = server_port

    def read_tcp(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the server
            s.connect((self.server_address, self.server_port))
            print("Connected to server at %s on port %s", self.server_address, self.server_port)
            
            while True:
                # Receive message from the server
                data = s.recv(1024)
                print(data)
                if not data:
                    # No more data from server, can happen if the server closes the connection
                    print("Disconnected from server")
                    break

                # Assuming the message is in JSON format

                # data = data.decode().replace("'", '"')
                # message = json.loads(data)
                # print("Received JSON message: %s", message)

                
                # Sleep for a second to manage timing and avoid spamming
                time.sleep(1)
    
    def read_log_csv(self, log_path: str, loops: int = 1):
        """Test method to read signals from CAN logs"""
        def convert_value(value):
            # Attempt to convert the value to an int, float, or leave as string
            try:
                if '.' in value:
                    return float(value)
                return int(value)
            except ValueError:
                return value

        initial_timestamp = None
        total_offset = 0

        for _ in range(loops):
            with open(log_path, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    timestamp_str, signal_name = parts[:2]
                    value = ','.join(parts[2:])

                    original_timestamp = float(timestamp_str)

                    if initial_timestamp is None:
                        # Set the initial timestamp based on the first log entry
                        initial_timestamp = original_timestamp

                    # Adjust the timestamp for current line including the total offset from previous loops
                    timestamp = original_timestamp - initial_timestamp + total_offset

                    value = convert_value(value)

                    print(f"Timestamp: {timestamp:.6f}, Signal Name: {signal_name}, Value: {value}")

            # After finishing each loop through the file, update the total_offset
            # This offset will be applied to timestamps in the next iteration
            total_offset = timestamp + (original_timestamp - initial_timestamp) - total_offset