def append_numbers_to_list(numbers_list, list):
    l = list.split()
    for num in l:
        numbers_list.append(int(num))
    
    return numbers_list


def generate_new_bingo_boards(lines):
    # Create list of BingoBoards
    boards, numbers_list = [], []
    for i in range(2, len(lines)):
        line = lines[i].replace('\n', '')
        if line == '':
            boards.append(BingoBoard(numbers_list))
            numbers_list = []
        else:
            numbers_list = append_numbers_to_list(numbers_list, line)

    return boards


def play_bingo(input, boards):
    for drawn in input:
        for board in boards:
            if not board.bingo:
                board.mark_drawn(drawn)
                if board.check_bingo():
                    board_score = board.calculate_score()
                    score = board_score * drawn
                    return score


def play_bingo_loser(input, boards):
    total_boards = len(boards)
    winning_boards_count = 0
    for drawn in input:
        for board in boards:
            if not board.bingo:
                board.mark_drawn(drawn)
                if board.check_bingo():
                    winning_boards_count += 1
                    if winning_boards_count == total_boards:
                        board_score = board.calculate_score()
                        score = board_score * drawn
                        return score


class BingoBoard:
    def __init__(self, numbers_list):
        if len(numbers_list) != 25:
            raise Exception("Not a valid Bingo board length!")

        self.board = [numbers_list[:5],
                 numbers_list[5:10],
                 numbers_list[10:15],
                 numbers_list[15:20],
                 numbers_list[20:25]]
        self.marked_board = [[False] * 5 for _ in range(5)]
        self.bingo = False


    def mark_drawn(self, drawn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == drawn:
                    self.marked_board[i][j] = True


    def check_bingo(self):
        if not self.bingo:
            row_marked_sums = []
            for i in range(len(self.board)):
                row_sum = 0
                for j in range(len(self.board[i])):
                    if self.marked_board[i][j]:
                        row_sum += 1
                row_marked_sums.append(row_sum)

            col_marked_sums = []
            for j in range(len(self.board[0])):
                col_sum = 0
                for i in range(len(self.board)):
                    if self.marked_board[i][j]:
                        col_sum += 1
                col_marked_sums.append(col_sum)

            self.bingo = 5 in row_marked_sums or 5 in col_marked_sums

        return self.bingo


    def calculate_score(self):
        score = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if not self.marked_board[i][j]:
                    score += self.board[i][j]

        return score


with open('./sources/aoc_p4.txt', 'r') as f:
    lines = f.readlines()
    input = list(map(int, lines[0].split(',')))
    
    boards_part_1 = generate_new_bingo_boards(lines)
    boards_part_2 = generate_new_bingo_boards(lines)

    print(f"Part 1 score is: {play_bingo(input, boards_part_1)}")
    print(f"Part 2 score is: {play_bingo_loser(input, boards_part_2)}")