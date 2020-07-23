from board import Board
from Round import Round
import random

class Game(object):
  def __init__(self, id, players):
    self.id = id
    self.players = players
    self.words_used = set()
    self.round = None
    self.board = Board()
    self.player_draw_ind = 0
    self.round_count = 1
    self.start_new_round()
    self.create_board()

  def start_new_round(self):
    round_word = self.get_word()
    self.round = Round(round_word, self.players[self.player_draw_id], self.players, self)
    self.player_draw_ind += 1
    self.round_count += 1

    if self.player_draw_ind >= len(self.player):
      self.round_ended()
      self.end_game()
  
  def get_player_score(self):
    scores = {player: player.get_score() for player in self.players}
    return scores

  def create_board(self):
    self.board = Board()
  
  def player_guess(self, player, guess):
    return self.round.guess(player, guess)

  def player_disconnected(self, player):
    if player in self.players:
      player_ind = self.players.index(player)
      if player_ind >= self.player_draw_ind:
        self.player_draw_ind -= 1
      self.players.remove(player)
      self.round.player_left(player)

    else:
      raise Exception('Player not in game.')

    if len(self.players) <= 2:
      self.end_game()

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
    for player in self.players:
      self.round.player_left(player)

  def get_word(self):
    with open('./words.txt', 'r') as f:
      words = []

      for line in f:
        wrd = line.strip()
        if wrd not in self.words_used:
          words.append(wrd)

      self.words_used.add(wrd)

      r = random.randint(0, len(words) - 1)
      return words[r].strip()