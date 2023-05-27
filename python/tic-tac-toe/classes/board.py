class Board:
    def __init__(self):
        self.area = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

    def display_area(self):
        for row in self.area:
            # for column in row:
            #     print(column, end='\t|')
            print('\t|\t'.join(row))
            print()