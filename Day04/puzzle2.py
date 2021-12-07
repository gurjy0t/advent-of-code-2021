from os import truncate
from typing import OrderedDict


def main():
    bingo_nums, boards = get_boards_and_nums_from_file("PuzzleDay4Input.txt")
    winning_boards = get_all_winning_boards(bingo_nums,boards)


    print(winning_boards[-1])
    losing_score = score_board(winning_boards[-1][0], winning_boards[-1][1])
    print(losing_score)



def score_board(marked_winning_board, winning_number):
    sum_unmarked = sum_all_unmarked(marked_winning_board)
    return sum_unmarked * winning_number

def sum_all_unmarked(board):
    tot = 0
    for row in board:
        for number in row:
            if number!=-1:
                tot+=number
    return tot

def get_all_winning_boards(bingo_nums, boards):
    winning_boards=[]
    winning_board_nums=[]
    while len(bingo_nums)!=0:
        drawn_num = bingo_nums.pop(0)

        for board_num in boards:
            if boards[board_num] != None:
                boards[board_num] = mark_board(boards[board_num], drawn_num)
                if has_board_won(boards[board_num]):
                    winning_boards.append((boards[board_num].copy(), drawn_num))
                    boards[board_num]=None
                    # winning_board=boards[board_num]
                    # if board_num not in winning_board_nums:
                        # winning_boards.append((boards[board_num].copy(), drawn_num))
                    #     winning_board_nums.append(winning_board_nums)
            # if winning_board_nums
                
                

    return winning_boards

def has_board_won(board):
    grid_size = len(board)
    i=0
    while i<grid_size:
        if has_all_marked(board[i]) or has_all_marked([j[i] for j in board]):
            return True
        i+=1
    return False

def has_all_marked(row):
    for number in row:
        if number!=-1: 
            return False
    return True

def mark_board(board, number):
    grid_size=len(board)
    i=0
    while i < grid_size:
        board[i] = mark_row(board[i], number)
        i+=1
    return board

def mark_row(row, number):
    row_len = len(row)
    i = 0
    while i < row_len:
        if row[i]==number:
            row[i]=-1
        i+=1
    return row


def get_boards_and_nums_from_file(filename):
    file = open(filename, "r")

    bingo_nums = []
    boards={}
    marker_boards={}
    board_num=1
    boards[board_num]=[]
    parsing_boards = False

    for line in file:
        if not parsing_boards:
            if line == '\n':
                parsing_boards = True
                continue
            for x in line.strip('\n').strip(' ').split(','):
                bingo_nums.append(int(x))
        else:
            if line == '\n':
                board_num += 1
                boards[board_num]=[]
                continue
            
            row = [int(x) for x in str.split(line.strip('\n'))]
            boards[board_num].append(row)

    
    file.close()

    return bingo_nums, boards

if __name__ == "__main__":
    main()
