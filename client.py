import asyncio
import websockets

## Function to handle the chat client
async def chat():
    async with websockets.connect('ws://localhost:12345') as websocket:
        while True:
            message = input("Enter message: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received: {response}")

if __name__ == "__main__":
    asyncio.run(chat())