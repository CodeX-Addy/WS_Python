# client.py
import asyncio
import websockets

async def send_and_receive():
    uri = "ws://localhost:12345"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")
        
        # Send a message
        await websocket.send(f"{name}: Hello everyone!")
        
        # Receive messages
        while True:
            try:
                message = await websocket.recv()
                print(f"< {message}")
            except websockets.exceptions.ConnectionClosed:
                print("Connection closed")
                break

async def main():
    await send_and_receive()

if __name__ == "__main__":
    asyncio.run(main())