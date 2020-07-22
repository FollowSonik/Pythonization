from .player import Player
from .board import Board
from .round import Round

class Game(object):
  def __init__(self, id, players, thread):
    self.id = id
    self.players = players
    self.words_used = []
    self.round = None
    self.board = Board()
    self.player_draw_ind = 0
    self.connected_thread = thread
    self.start_new_round()
    self.create_board()

  def start_new_round(self):
    self.round = Round(self.get_word(), self.players[self.player_draw_id], self.players, self)
    self.player_draw_ind += 1

    if self.player_draw_ind >= len(self.player):
      self.round_ended()
      self.end_game()

  def create_board(self):
    self.board = Board()
  
  def player_guess(self, player, guess):
    return self.round.guess(player, guess)

  def player_disconnected(self, player):
    pass

  def skip(self):
    if self.round:
      new_round = self.round.skip()
      if new_round:
        self.round_ended()
    else:
      raise Exception('No round started yet!')

  def round_ended(self):
    self.start_new_round()
    self.board.clear()


  def update_board(self, x, y, color):
    if self.board:
      raise Exception('No board created.')
    self.board.update(x, y, color)

  def end_game(self):
    pass

  def get_word(self):
    pass