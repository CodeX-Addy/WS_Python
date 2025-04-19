# client.py
import asyncio
import websockets

## Function to handle the chat client
async def chat():
    async with websockets.connect('ws://localhost:12345') as websocket:
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
    asyncio.run(chat())