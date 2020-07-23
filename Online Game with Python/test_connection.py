import socket
import json

class Network:
  def __init__(self, name):
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.server = 'localhost'
    self.port = 3228
    self.addr = (self.server, self.port)
    self.name = name
    self.connect()

  def connect(self):
    try:
      self.client.connect(self.addr)
      self.client.sendall(self.name.encode())
      return json.loads(self.client.recv(2048))
    except Exception as e:
      self.disconnect(e)

  def send(self, data):
    try:
      self.client.send(data.encode())
      return json.loads(self.client.recv(2048))
    except socket.error as e:
      self.disconnect(e)

  def disconnect(self, msg):
    print('[EXCEPTION] Disconnected from server.', msg)
    self.client.close()

n = Network('FollowSonik')
print(n.connect())
print(n.send('{0:[]}'))