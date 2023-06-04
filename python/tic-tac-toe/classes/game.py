class Game:
    STARTING_SYMBOL = 'O'

    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.current_player = player1 if self.player1.symbol == self.STARTING_SYMBOL else player2

    def play(self):
        while not self.board.is_full():
            print("Aktualny gracz jest gracz z symbolem " +
                  self.current_player.symbol)

            row = int(input("W którym rzędzie chciałbyś postawić swój symbol:\n"))
            column = int(
                input("W której kolumnie chciałbyś postawić swój symbol:\n"))

            while not self.board.area[row][column] == '':
                print("To miejsce na planszy jest już zajęte.\n")
                row = int(
                    input("Podaj inny rząd, w którym chciałbyś postawić swój symbol:\n"))
                column = int(
                    input("Podaj inną kolumnę, w której chciałbyś postawić swój symbol:\n"))

            self.board.area[row][column] = self.current_player.symbol
            self.board.display_area()

            if self.board.has_winner(self.current_player.symbol):
                print("Gracz "+self.current_player.symbol+" jest zwycięzcą!")
                exit()

            self.current_player = self.player1 if self.player1.symbol != self.current_player.symbol else self.player2

        print("Remis")
