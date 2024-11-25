import socket

def start_server(host='127.0.0.1', port=12345, backlog=5):
    """
    Starts a TCP server to handle incoming client connections.
    """
    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Bind the socket to the provided host and port
            server_socket.bind((host, port))
            # Start listening for incoming connections
            server_socket.listen(backlog)
            print(f"Server is listening on {host}:{port}...")

            # Accept a single client connection
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connection established with {client_address}")

                # Receive data from the client
                data = client_socket.recv(1024).decode('utf-8')
                if data:
                    print(f"Received: {data}")
                    # Echo the received data back to the client
                    client_socket.send(data.encode('utf-8'))
                else:
                    print("No data received.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        print("Server shutting down...")

if __name__ == "__main__":
    start_server()
