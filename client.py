import socket

def communicate_with_server(host='127.0.0.1', port=12345, message="Hello, Server!"):
    """
    Connects to the server, sends a message, and receives a response.
    """
    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # Connect to the server
            client_socket.connect((host, port))
            print(f"Connected to server at {host}:{port}")

            # Send a message to the server
            client_socket.send(message.encode('utf-8'))
            print(f"Sent to server: {message}")

            # Receive the server's response
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Received from server: {response}")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        print("Closing connection...")

if __name__ == "__main__":
    communicate_with_server()
