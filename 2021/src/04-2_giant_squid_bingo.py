import pandas as pd

board_file = open(r'../input/04_giant_squid_bingo_boards.txt')
number_file = open(r'../input/04_giant_squid_bingo_numbers.txt')

boards_raw = board_file.read().splitlines()
numbers_raw = [int(x) for x in number_file.read().split(',')]


def read_board_line(line):
    return [int(x) for x in boards_raw[line].split()]


# Create boards
boards = []
for row1 in range(0, len(boards_raw), 6):
    df = pd.DataFrame([read_board_line(row1),
                      read_board_line(row1+1),
                      read_board_line(row1+2),
                      read_board_line(row1+3),
                      read_board_line(row1+4)])
    df_bool = df.copy()
    df_bool.loc[:, :] = False
    boards.append([df, df_bool])


def call_numbers(numbers, boards):
    winning_boards = []
    for call_number in numbers:
        for i, board in enumerate(boards):
            # Update Board
            num_board = board[0]
            bool_board = board[1]
            bool_board = (num_board == call_number) | bool_board
            board[1] = bool_board

            # Check for bingo
            horizontal_bingo = bool_board.all(axis=1).any()
            vertical_bingo = bool_board.all(axis=0).any()
            bingo = (horizontal_bingo or vertical_bingo) and (i not in winning_boards)

            if bingo:
                unmarked_nums_sum_and_call_number = num_board[~bool_board].sum().sum() * call_number
                winning_boards.append(i)
    return unmarked_nums_sum_and_call_number


print(f'Part 2 answer: {call_numbers(numbers_raw, boards)}')
