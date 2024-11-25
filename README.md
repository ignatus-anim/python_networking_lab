# **Socket Programming: Simple Client-Server Application**

This project demonstrates a basic client-server communication using Python's `socket` module. The server listens for incoming client connections and echoes back the messages it receives. The client connects to the server, sends a message, and receives a response.

---

## **Features**
- **Server**:
  - Listens for incoming TCP connections.
  - Accepts and processes a single client at a time.
  - Echoes back received messages.
- **Client**:
  - Connects to the server.
  - Sends a customizable message.
  - Receives and displays the server's response.

---

## **Requirements**
- **Python 3.x**
- No additional libraries are needed; this project uses Python's standard library.

---

## **Setup and Usage**

### **1. Clone the Repository**
```bash
git clone <repository_url>
cd <repository_directory>
```

### **2. Run the Server**
1. Open a terminal and navigate to the project directory.
2. Start the server:
   ```bash
   python server.py
   ```
3. The server will begin listening for incoming connections on `127.0.0.1:12345`.

### **3. Run the Client**
1. Open a separate terminal and navigate to the project directory.
2. Start the client:
   ```bash
   python client.py
   ```
3. The client will connect to the server, send a message, and display the server's response.

---

## **Code Explanation**

### **Server (`server.py`)**
- Creates a **TCP socket** using `socket.AF_INET` and `socket.SOCK_STREAM`.
- Binds the socket to the specified host (`127.0.0.1`) and port (`12345`).
- Listens for incoming connections with a backlog of 5.
- Accepts a client connection, receives a message, and sends the message back (echo functionality).
- Closes the connection and shuts down gracefully.

### **Client (`client.py`)**
- Creates a **TCP socket** to connect to the server.
- Sends a customizable message (`"Hello, Server!"` by default).
- Waits for the server's response and displays it.
- Closes the connection gracefully.

---

## **Customization**
1. **Server Configuration**:
   - Change the `host` or `port` in the `start_server` function:
     ```python
     start_server(host='0.0.0.0', port=8080)
     ```
2. **Client Configuration**:
   - Modify the `host`, `port`, or `message` in the `communicate_with_server` function:
     ```python
     communicate_with_server(host='192.168.1.1', port=8080, message="Custom Message")
     ```

---

## **Output Example**

### **Server Output**
```
Server is listening on 127.0.0.1:12345...
Connection established with ('127.0.0.1', 56789)
Received: Hello, Server!
Server shutting down...
```

### **Client Output**
```
Connected to server at 127.0.0.1:12345
Sent to server: Hello, Server!
Received from server: Hello, Server!
Closing connection...
```

---

## **Improvements and Extensions**
- **Handle Multiple Clients**:
  - Use threading or asynchronous programming (`asyncio`) to handle multiple client connections simultaneously.
- **Enhanced Communication**:
  - Add support for message termination signals or protocols (e.g., HTTP-like communication).
- **Error Recovery**:
  - Improve error handling to handle connection drops or invalid data.
- **Secure Communication**:
  - Use SSL/TLS to encrypt data exchanged between the client and server.

---

## **License**
This project is licensed under the MIT License. Feel free to use and modify the code for your needs.

---

## **Author**
**Ignatus Anim**  
Email: [ignatus.anim@amalitech.com](mailto:ignatus.anim@amalitech.com)  

For any questions or feedback, feel free to reach out!