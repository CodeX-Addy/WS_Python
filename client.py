import asyncio
import websockets

## Function to handle sending messages
async def sender(websocket):
    while True:
        message = input("Enter message: ")
        await websocket.send(message)
        await asyncio.sleep(0.1)

## Function to handle receiving messages
async def receiver(websocket):
    while True:
        try:
            message = await websocket.recv()
            print(f"< {message}")
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")
            break

## Main chat function to handle both sending and receiving
async def chat():
    async with websockets.connect('ws://localhost:12345') as websocket:
        sender_task = asyncio.create_task(sender(websocket))
        receiver_task = asyncio.create_task(receiver(websocket))
        await asyncio.gather(sender_task, receiver_task)

if __name__ == "__main__":
    try:
        asyncio.run(chat())
    except KeyboardInterrupt:
        print("\nClient stopped by user")
    except Exception as e:
        print(f"Error: {e}")