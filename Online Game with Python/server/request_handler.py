import socket
import threading
from player import Player
from game import Game
import json

class Server(object):
  PLAYERS = 8
  def __init__(self):
    self.connection_queue = []
    self.game_id = 0

  def player_thread(self, conn, player):
    while True:
      try:
        data = conn.recv(1024)
        data = json.loads(data.decode())

        keys = [key for key in data.keys()]
        send_msg = {key: [] for key in keys}

        for key in keys:
          if key == -1:
            if player.game:
              send_msg[-1] = player.game.players
            else:
              send_msg[-1] = []
          
          if player.game:
            if key == 0:
              correct = player.game.player_guess(player, data[0][0])
              send_msg[0] = correct

            elif key == 1:
              skip = player.game.skip()
              send_msg[1] = skip

            elif key == 2:
              content = player.game.round.chat.get_chat()
              send_msg[2] = content 

            elif key == 3:
              brd = player.game.board.get_board()
              send_msg[3] = brd

            elif key == 4:
              scores = player.game.get_player_scores()
              send_msg[4] = scores

            elif key == 5:
              rnd = player.game.round_count
              send_msg[5] = rnd

            elif key == 6:
              word = player.game.round.word
              send_msg[6] = word

            elif key == 7:
              skips = player.game.round.skips
              send_msg[7] = skips

            elif key == 8:
              x, y, color = data[8][:3]
              self.game.update_board(x, y, color)

            elif key == 9:
              t = self.game.round.time
              send_msg[9] = t

            else:
              raise Exception('Not a valid request.')
              conn.close()

        conn.sendall(json.dumps(send_msg))
      except Exception as e:
        print(f'[EXCEPTION {player.get_name()} disconnected:', e)
        conn.shutdown(socket.SHUT_RDWR)
        break

  def handle_queue(self, player):
    self.connection_queue.append(player)

    if len(self.connection_queue) >= self.PLAYERS:
      game = Game(self.connection_queue[:], self.game_id)

      for p in self.connection_queue:
        p.set_game(game)

      self.game_id += 1
      self.connection_queue = []


  def authentication(self, conn, addr):
    try:
      data = conn.recv(1024)
      name = str(data.decode())
      if not name:
        raise Exception('No name received.')

      conn.sendall('1'.encode())
      player = Player(addr, name)
      self.handle_queue(player)
      thread = threading.Thread(target=self.player_thread, args=(conn, player))
      thread.start()

    except Exception as e:
      print('[EXCEPTION]', e)
      conn.shutdown(socket.SHUT_RDWR)
      conn.close()

  def connection_thread(self):
    server = 'localhost'
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

      self.authentication(conn, addr)

if __name__ == '__main__':
  s = Server()
  thread = threading.Thread(target=s.connection_thread) 
  thread.start()