import socket

s = socket.socket()
port = 12345
s.bind(('', port))
print ("Listening for connections")
s.listen(5)

c, addr = s.accept()
print ("Socket Up and running with a connection from",addr)
while True:
    try:
        rcvdData = c.recv(1024).decode()
    except:
        print("User has disconnected")
        break
    print ("S:",rcvdData)
    sendData = input("N: ")
    c.send(sendData.encode())
    if(sendData == "Bye" or sendData == "bye"):
        break
c.close()
