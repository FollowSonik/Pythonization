import socket
import time
import threading
from .player import Player
from .game import Game
from queue import Queue

def player_thread(conn, ip):
  pass

def authentication(conn, addr):
  try:
    data = conn.recv(16)
    name = str(data.decode())
    if not name:
      raise Exception('No name received.')

    conn.sendall('1'.encode())
    threading.Thread(target=player_thread, args=(conn, addr, name))

  except Exception as e:
    print('[EXCEPTION]', e)
    conn.close()

def connection_thread():
  server = ''
  port = 3228

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    s.bind((server, port))
  except:
    str(e)

  s.listen()
  print('Pog!')

  while True:
    conn, addr = s.accept()
    print('[LOG] New connection!')

    authentication(conn, addr)

if __name__ == '__main__':
  threading.Thread(target=connection_thread()) 