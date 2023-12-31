from classes.player import Player
from classes.game import Game
from classes.board import Board

player1 = Player("X")
player2 = Player("O")
board = Board()
game = Game(player1, player2, board)
game.play()
