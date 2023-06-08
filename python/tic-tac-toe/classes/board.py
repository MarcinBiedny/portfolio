class Board:
    def __init__(self):
        self.area = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

    def display_area(self):
        for row in self.area:
            print('\t|\t'.join(row))
            print()

    def is_full(self):
        for row in self.area:
            for cell in row:
                if cell == '':
                    return False
        return True

    def has_winner(self, symbol):
        if self.area[0][0] == self.area[0][1] == self.area[0][2] == symbol \
                or self.area[1][0] == self.area[1][1] == self.area[1][2] == symbol \
                or self.area[2][0] == self.area[2][1] == self.area[0][2] == symbol:
            return True
        if self.area[0][0] == self.area[1][0] == self.area[2][0] == symbol \
                or self.area[0][1] == self.area[1][1] == self.area[2][1] == symbol \
                or self.area[0][2] == self.area[1][2] == self.area[2][0] == symbol:
            return True
        if self.area[0][0] == self.area[1][1] == self.area[2][2] == symbol \
                or self.area[0][2] == self.area[1][1] == self.area[2][0] == symbol:
            return True
        return False
