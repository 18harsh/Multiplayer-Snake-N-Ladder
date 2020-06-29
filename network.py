import socket



class Network:
	def __init__(self):
		self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.server = socket.gethostbyname(socket.gethostname())
		self.port = 5555
		self.addr = (self.server,self.port)
		self.score = self.connect()
		
	def getPos(self):
		return self.score

	def connect(self):
		try:
			self.client.connect(self.addr)
			return self.client.recv(4096).decode()
		except:
			pass

	def send(self, data):
		try:
			self.client.send(str.encode(data))
			return self.client.recv(4096).decode()
		except socket.error as e:
			print(e)

