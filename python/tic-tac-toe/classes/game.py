class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def play(self):
        row = int(input("W którym rzędzie chciałbyś postawić swój symbol:\n"))
        column = int(input("W której kolumnie chciałbyś postawić swój symbol:\n"))
        self.board.area[row][column] = self.player1.symbol
        self.board.display_area()