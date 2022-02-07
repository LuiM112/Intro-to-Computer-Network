import socket
import threading

host = "127.0.0.1"
port = 5000
address = (host, port)
size = 1024
format = "utf-8"
disconnect_msg = "!bye"
count = 1

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        retMsg = ""
        msg = conn.recv(size).decode(format)
        if msg == disconnect_msg:
            connected = False

        print(f"[{addr}] sent message {count}: {msg}")
        if count == 1:
            retMsg = f"From server: {addr} {msg}"

        if count == 2:
            retMsg = f"{retMsg} received before {addr}: {msg}"

        conn.send(retMsg.encode(format))
        count+1

    conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(address)
    print("The Server is waiting to receive 2 connections...")
    server.listen()
    
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == '__main__':
    main()