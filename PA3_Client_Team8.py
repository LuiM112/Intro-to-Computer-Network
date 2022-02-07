import socket

host = "127.0.0.1"
port = 5000
address = (host, port)
size = 1024
format = "utf-8"
disconnect_msg = "!bye"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(address)
    print(f"[CONNECTED] client connected to server at {host} : {port}")

    connected = True
    while connected:
        msg = input("> ")

        client.send(msg.encode(format))

        if msg == disconnect_msg:
            connected = False
        else:
            msg = client.recv(size).decode(format)
            print(f"[SERVER] {msg}")

if __name__ == "__main__":
    main()
