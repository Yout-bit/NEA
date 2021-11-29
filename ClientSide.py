import socket

s = socket.socket()
s.connect(('127.0.0.1',12345))
while True:
    stri = True
    s.send(stri.encode());
    if(stri == "Bye" or stri == "bye"):
        break
    try:
        print ("N:",s.recv(1024).decode())
    except:
        print("User has disconnected")
        break
s.close()
