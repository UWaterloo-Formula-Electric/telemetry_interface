import socket
import time

def start_server(host='0.0.0.0', port=12345):
    print("Attempting to start server")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((host, port))
    
    server_socket.listen(5)
    
    print(f"Server listening on {host}:{port}")
    
    try:
        while True:
            # Accept a connection from a client
            client_socket, addr = server_socket.accept()
            print(f"Connected by {addr}")
            
            try:
                while True:
                    # Message to be sent
                    message = b'0x18C0040110C432AE32BB3200,0x18C0040110C432AE32BB3200,0x18C0040110C432AE32BB3200,'
                    # Send the message to the client
                    client_socket.sendall(message)
                    # Wait a bit before sending the next one
                    time.sleep(1)
            except socket.error as e:
                print(f"Socket error: {e}")
            finally:
                client_socket.close()
                print(f"Disconnected from {addr}")
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()

if __name__ == '__main__':
    start_server()