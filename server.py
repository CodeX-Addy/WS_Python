import asyncio
import websockets

## Set of connected clients
connected_clients = set()

## Function to handle each client connection
async def handle_client(websocket):
    connected_clients.add(websocket)
    try:
        ## Listen for messages from the client side
        async for message in websocket:
            print(f"Received message: {message}")
            ## Broadcast the message to all other connected clients
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

## Main function to start the WebSocket server
async def main():
    server = await websockets.serve(
        handle_client, 
        'localhost', 
        12345
    )
    print("WebSocket server started at ws://localhost:12345")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
