import socket

s = socket.socket()
print('Socket is Created')
s.bind(('localhost',9999))
s.listen(3)

while True:
    c,add = s.accept()
    name = c.recv(1024).decode()
    print('connected with',add,name)
    c.send(bytes('you are connected to Vampie server','utf-8'))
    c.close()