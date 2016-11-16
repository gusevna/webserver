import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('127.0.0.1', 2222))
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data: break
        if data == b"close":
#            print ("Close connection")
            break
        conn.send(data)
#        print (data)
    conn.close()
