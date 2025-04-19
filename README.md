# Web Sockets in Python

### Web Sockets are a protocol for full-duplex communication channels over a single TCP connection.They are commonly used in real-time web applications, such as chat applications, online gaming, and live notifications.Web Sockets allow for low-latency communication between the client and server, enabling real-time updates without the need for constant polling.
### In this example, we will create a simple WebSocket server and client using Python.


### The server listens for incoming connections and echoes back any messages it receives.

### The client connects to the server and sends a message, then waits for a response.

### The server and client are implemented using the `websockets` library.



### To use this code, you need to install the following packages:
- websockets
- asyncio

### To install the packages, run the following command:
```bash
pip install websockets asyncio
```

### To run the code, use the following command:
```bash
python -m websockets.server --port 8765 server.py
```
```bash
python -m websockets.client --port 8765 client.py
```


