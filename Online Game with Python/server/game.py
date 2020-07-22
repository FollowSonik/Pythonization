from .player import Player
from .board import Board
from .round import Round
import random

class Game(object):
  def __init__(self, id, players, thread):
    self.id = id
    self.players = players
    self.words_used = set()
    self.round = None
    self.board = Board()
    self.player_draw_ind = 0
    self.connected_thread = thread
    self.start_new_round()
    self.create_board()

  def start_new_round(self):
    round_word = self.get_word()
    self.round = Round(round_word, self.players[self.player_draw_id], self.players, self)
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
    with open('words.txt', 'r') as f:
      words = []

      for line in f:
        wrd = line.strip()
        if wrd not in self.words_used:
          words.append(wrd)

      self.words_used.add(wrd)

      r = random.randint(0, len(words))
      return words[r].strip()