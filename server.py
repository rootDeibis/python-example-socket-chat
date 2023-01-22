import socket
import threading

import os
import signal


host = socket.gethostname()
port = 3000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()


clients = []


def clear():
    for i in range(50):
        print("\r")


def broadcast(message, _client):
    for client in clients:
        try:
            if client != _client:
                client.send(message)
        except:
            clients.remove(client)


def handle_client_message(client: socket.socket, addr):
    while True:
        try:
            output = client.recv(1024)
            if len(output) > 0:
                print(f"Sending new message coming from address: {addr}")
                broadcast(output, client)
        except:
            client.close()
            clients.remove(client)
            break



def handle_connection():
    while True:
        conn, addr = server.accept()
        clients.append(conn)

        print(f"Registered new connection from: {addr}")

        client_thread = threading.Thread(target=handle_client_message, args=(conn,addr,))

        client_thread.start()



def run_start():
    thread = threading.Thread(target=handle_connection)
    thread.start()

run_start()