import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 9090))
conn.listen(10)

while True:
	try:
		clientsocket, address = conn.accept()
		data = clientsocket.recv(1024)
		udata = data.decode("utf-8")
		print(udata)
		clientsocket.send(b"Hello, client")
		clientsocket.close()
	except KeyboardInterrupt:
		conn.close()
		break