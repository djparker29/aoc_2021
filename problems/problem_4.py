class BingoBoard:
    def __init__(self, numbers):
        self.numbers = numbers 


with open('./sources/aoc_p4.txt', 'r') as f:
    lines = list(map(lambda x: int(x.replace('\n', '')), f.readlines()))
    boards = []
    for line in lines:
        board = BingoBoard(line)
        boards.append(board)