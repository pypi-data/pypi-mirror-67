# packetsocket

High-level socket interface for non-blocking packet communication.

[Github](https://github.com/Dead-Man-Walker/python-packetsocket)

## Description

packetsocket provides a simple, high-level class interface for non-blocking
sockets communicating in packet messages. Two types of sockets
are implemented: `PacketSocketServer` and `PacketSocketClient`. A server can accept incoming
client connections, a client can connect to one server. Both inherit the common PacketSocket
operations (`open`, `close`, `update`, `read`, `write`) from the base class `PacketSocket`.
These methods are thread-safe using an internal lock.

PacketSockets work in non-blocking mode regarding the sending and receiving of socket messages.
They do, however, have the option to block while waiting for the lock.

PacketSockets communicate messages as simple packets. They are composed as follows:
"<HEADER_PREFIX><body-size><body>"
where <HEADER_PREFIX> is the constant bytestring `PacketSocket.HEADER_PREFIX` identifying the
beginning of a new message, <body-size> stores the size of the body of a fixed length of
`PacketSocket.HEADER_BYTES` bytes, and <body> is the message itself.


## Example

```python3

from queue import Queue
from threading import Thread

from packetsocket import Server, Client

ADDRESS = ("", 4200)
messages = Queue()
running = True


def runServer(messages, address, running):
    with Server(address) as server:
        while running:
            while not messages.empty():
                msg = messages.get_nowait()
                server.write(msg)

            server.update()

            for sock, msgs in server.read():
                client_name = sock.getpeername()[0]
                for msg in msgs:
                    print(f"[{client_name}] {msg.decode()}")


def runClient(messages, address, running):
    with Client(ADDRESS) as client:
        while running:
            client.update()

            for msg in client.read():
                print(f"[Server] {msg.decode()}")
                client.write(b"<Server Echo> " + msg)


def getInput(messages, running):
    while running:
        inp = input("Send message to client: \n")
        if inp.strip():
            messages.put(inp.encode())
            print("\n")


try:
    Thread(target=getInput, args=(messages, running)).start()
    Thread(target=runServer, args=(messages, ADDRESS, running)).start()
    Thread(target=runClient, args=(messages, ADDRESS, running)).start()
finally:
    running = False

```
