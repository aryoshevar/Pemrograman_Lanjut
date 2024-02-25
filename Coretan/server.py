import socket

server_adress = ('localhost',4999)

SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(server_adress)

s.listen(5)

print ('Waiting for connection')

client, client_address = s.accept()
print ('Connected from : ', client_address)

while 1:    
    message = client.recv(SIZE)
    # message = message.decode()
    if(message == '1'):
        balik = 'Hello Juga'
    else:
        balik = 'Input salah'
        
    if not message : break
    print (message)
    client.send(balik.encode())
    # print(socket.gethostbyname())
    
s.close()