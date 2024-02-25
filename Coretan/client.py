import socket

server_address = ('localhost',4999)

SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)

while 1:
    print ("1.Hello Server")

    menu = input("Pilih menu:")

    if not menu: break
    s.send(menu.encode())

    message = s.recv(SIZE)
    message = message.decode()

    if not message: break
    print(message)

s.close