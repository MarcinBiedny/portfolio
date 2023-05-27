class Game:
    STARTING_SYMBOL = 'O'
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.current_player = player1 if self.player1.symbol == self.STARTING_SYMBOL else player2

    def play(self):
        board_full = 9
        






        row = int(input("W którym rzędzie chciałbyś postawić swój symbol:\n"))
        column = int(input("W której kolumnie chciałbyś postawić swój symbol:\n"))
        self.board.area[row][column] = self.player1.symbol
        self.board.display_area()
