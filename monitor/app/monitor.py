import socket
import json
import time
from datetime import datetime
from can_data import Signal, DBC
from influx_writer import write_signal, write_dtc

class Monitor:
    def __init__(self, server_address: str, server_port: int, dbc_path: str):
        self.server_address: str = server_address
        self.server_port: int = server_port
        self.dbc: DBC = DBC(dbc_path)

    def read_tcp(self):
        """Read data from the TCP server"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the server
            s.connect((self.server_address, self.server_port))
            print(f"Connected to server at {self.server_address} on port {self.server_port}")
            
            buffer = ''
            while True:
                # Receive message from the server
                data = s.recv(1024)
                buffer += data.decode().replace('\n','')
                print(buffer)
                while ',' in buffer:
                    # Find the position of the delimiter indicating the end of a message
                    delimiter_position = buffer.find(',')
                    # Extract the message up to the delimiter
                    message = buffer[:delimiter_position]
                    # Check it is well formed
                    if 'x' not in message or len(message.split('x')) != 2:
                        buffer = buffer[delimiter_position + len(','):]
                        continue
                    # Process the message
                    self.process_can_message(message)
                    # Remove the processed message from the buffer
                    buffer = buffer[delimiter_position + len(','):]
           
    
    def _process_message(self, message: str) -> tuple:
        if 'x' not in message or len(message.split('x')) != 2:
            return None, None, None
        else:
            timestamp = message[:8]
            clean_hex = message[9:]

            id_hex = clean_hex[:8]
            data_hex = clean_hex[8:]

            id_int = int(id_hex, 16)
            data_int = int(data_hex, 16)
            print("Received msg id: ", id_int, " data: ", data_int, " timestamp: ", timestamp)
            return id_int, data_hex, timestamp
    
    def process_can_message(self, message: str):
        def is_dtc(msg_name: str) -> bool:
            return 'DTC' in msg_name
        
        can_id, can_data, timestamp = self._process_message(message)
        if can_id is None:
            return
        if can_id == 218103553:
            print(f"Skipping message with frame ID: {can_id}")
            return

        try:
            msg = self.dbc.cantools_db.get_message_by_frame_id(can_id)
        except KeyError:
            print(f"Frame ID {can_id} not found in DBC file")
            return

        data_bytes = bytes.fromhex(can_data)
        decoded_signals = msg.decode(data_bytes)

        if is_dtc(msg.name):
            write_dtc(decoded_signals['DTC_CODE'], decoded_signals['DTC_Severity'], decoded_signals['DTC_Data'], msg.name)
        else:
            for signal_name, signal_value in decoded_signals.items():
                timestamp = datetime.now().timestamp()
                signal = Signal(signal_name, signal_value, timestamp, self.dbc)
                write_signal(signal)


    def simulate_telemetry(self, log_path: str):
        """Test method to simulate telemetry data"""
        def convert_value(value):
            try:
                if '.' in value:
                    return float(value)
                return int(value)
            except ValueError:
                return value

        # Get the current time
        start_time = datetime.now().timestamp()

        # Initialize variables to store the initial and last timestamps from the log file
        initial_timestamp_log = None
        last_timestamp_log = 0

        with open(log_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                timestamp_str, signal_name = parts[:2]
                value = ','.join(parts[2:])

                original_timestamp = float(timestamp_str)

                if initial_timestamp_log is None:
                    initial_timestamp_log = original_timestamp

                # Calculate the time difference from the last log entry
                time_difference = original_timestamp - initial_timestamp_log

                # Calculate the real-time timestamp adjustment
                adjusted_timestamp = start_time + time_difference

                # Calculate the delay needed before sending the next data
                delay = adjusted_timestamp - (start_time + last_timestamp_log)

                # Wait for the time offset from the last entry before proceeding
                if delay > 0:
                    time.sleep(delay)

                last_timestamp_log = time_difference

                value = convert_value(value)

                # Call the send_data function with the adjusted timestamp

                signal = Signal(signal_name, value, adjusted_timestamp, self.dbc)
                write_signal(signal)

    def simulate_random(self):
        """Test method to simulate random telemetry data"""
        while 1:
            for frame in self.dbc.dbc.frames:
                if frame.name == 'VECTOR__INDEPENDENT_SIG_MSG':
                    continue
                if 'DTC' in frame.name:
                    write_dtc(2, 1, 0, 'PDU_DTC')
                else:
                    pass
                time.sleep(0.1)
                    # for signal in frame.signals:
                    #     write_signal(Signal(signal.name, random.randint(0, 100), datetime.now().timestamp(), self.dbc))

if __name__ == '__main__':
    monitor = Monitor('localhost', 12345, 'path_to_dbc_file.dbc')
    monitor.read_tcp()
