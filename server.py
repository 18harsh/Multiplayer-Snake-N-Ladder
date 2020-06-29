import socket
from _thread import *
import sys

server = socket.gethostbyname(socket.gethostname())
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	s.bind((server,port))
except socket.error as e:
	print(e)

s.listen(2)
print("Waiting for a connection \nserver started...")

def read_pos(str):
    return int(str[0])


def make_pos(tup):
    return str(tup[0])

score = [(0),(0)]

def threaded_client(conn,player):
	conn.send(str.encode(str(score[player])))
	reply = ""
	while True:
		# print(player)
		try:
			data = int(conn.recv(4096).decode())
			score[player] = data

			if data =="":
				print("Disconnected")
				break
			else:
				if player == 1:
					reply = score[0]
				else:
					reply = score[1]
				print("Received: ", data)
				print("sending: ",reply)

			conn.sendall(str.encode(str(reply)))

		except:
			break

	print("Lost connection")
	conn.close()

currentPlayer = 0
while True:
	conn, addr = s.accept()
	print("Connected to:",addr)

	start_new_thread(threaded_client,(conn,currentPlayer))
	currentPlayer += 1