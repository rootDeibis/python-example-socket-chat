import socket
from threading import Thread
import os

host = socket.gethostname()
port = 3000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))



def handle_server_message():
    while True:
        message = client.recv(1024).decode("utf-8")
        if len(message) > 2:
            print(f"MSG > {message}")


thread = Thread(target=handle_server_message)

thread.start()


while True:
    message = input("")

    if len(message) > 0:
       try:
        client.send(bytes(message, "utf-8"))
       except:
        print("Error has been ocurred")
     