import asyncio
import websockets
import http

## Set of connected clients
connected_clients = set()

## Function to handle each client connection
async def handle_client(websocket, path):
    ## Add the new client to the set of connected clients
    connected_clients.add(websocket)
    try:
        ## Listen for messages from the client
        async for message in websocket:
            ## Broadcast the message to all other connected clients
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        ## Remove the client from the set of connected clients
        connected_clients.remove(websocket)

## Process HTTP requests - respond with a friendly message for browsers
async def process_request(path, request_headers):
    if "Upgrade" not in request_headers or request_headers["Upgrade"].lower() != "websocket":
        return http.HTTPStatus.BAD_REQUEST, {}, b"This server only supports WebSocket connections\n"
    return None

## Main function to start the WebSocket server
async def main():
    server = await websockets.serve(
        handle_client, 
        'localhost', 
        12345,
        process_request=process_request
    )
    print("WebSocket server started at ws://localhost:12345")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())