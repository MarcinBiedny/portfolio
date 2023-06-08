class Game:
    STARTING_SYMBOL = 'O'
    MAX_ROW = 2
    MAX_COLUMN = 2

    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.current_player = player1 if self.player1.symbol == self.STARTING_SYMBOL else player2

    def play(self):
        while not self.board.is_full():
            print("Welcome to the game!")
            print("The current player is the player with the "+self.current_player.symbol+" symbol.")

            row = int(input("Which row would you like to place your symbol on?\n"))
            while not row <= self.MAX_ROW:
                row = int(input("Movement off the board. Enter another row:\n"))
            
            column = int(input("In which column would you like to place your symbol?\n"))
            while not column <= self.MAX_COLUMN:
                column = int(input("Movement off the board. Enter another column:\n"))

            while not self.board.area[row][column] == '':
                print("This space on the board is already occupied.\n")
                row = int(input("Enter a different row where you would like to place your symbol:\n"))
                while not row <= self.MAX_ROW:
                    row = int(input("Movement off the board. Enter another row:\n"))
                column = int(input("Enter another column where you would like to place your symbol:\n"))
                while not column <= self.MAX_COLUMN:
                    column = int(input("Movement off the board. Enter another column:\n"))

            self.board.area[row][column] = self.current_player.symbol
            self.board.display_area()

            if self.board.has_winner(self.current_player.symbol):
                print("Player "+self.current_player.symbol+" is the winner!")
                exit()

            self.current_player = self.player1 if self.player1.symbol != self.current_player.symbol else self.player2

        print("DRAW")
