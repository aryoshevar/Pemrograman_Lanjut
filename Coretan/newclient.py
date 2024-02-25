import socket
import pandas as pd
import os

def receive_file(connection):
    file_size = int(connection.recv(1024).decode())
    received_size = 0

    with open('received_file.csv', 'wb') as file:
        while received_size < file_size:
            data = connection.recv(1024)
            received_size += len(data)
            file.write(data)

def main():
    server_address = ('172.19.15.100', 40100)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(server_address)

    s.send('1'.encode()) # Assuming we want to request file 'Book1.csv' from the server

    receive_file(s)

    s.close()

if __name__ == 'main':
    main()

df = pd.read_csv('received_file.csv')
print(df)