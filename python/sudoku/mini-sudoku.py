SIZE = 4
board1 = [[1, 0, 3, 0], [3, 0, 0, 2], [4, 3, 2, 1], [0, 0, 0, 3]]
board2 = [[0, 1, 3, 2], [2, 0, 1, 0], [1, 0, 0, 3], [3, 4, 2, 1]]
board3 = [[0, 0, 0, 0], [0, 1, 2, 4], [0, 3, 4, 1], [0, 4, 0, 2]]

def fill_row(board):
    def check_single_zero(insert_list):
        num_of_zeroes = 0
        for num in insert_list:
            if num == 0:
                num_of_zeroes += 1
        if num_of_zeroes == 1:
            return True
        else:
            return False
    
    def find_missing_num(insert_list):
        dict_of_nums = {1:0, 2:0, 3:0, 4:0, 0:0}
        counter = 0
        zero_index = 0
        for num in insert_list:
            dict_of_nums[num] += 1
            if num == 0:
                zero_index = counter
            counter+=1
                
        for num, times in dict_of_nums.items():
            if times == 0:
                return [zero_index, num]
    
    changes = 0
    for row in board:
        if check_single_zero(row):
            details = find_missing_num(row)
            row[details[0]] = details[1]
            changes +=1
        else:
            pass
    if changes == 0:
        return False
    else:
        return True

def fill_col(board):
    rev_board = list(map(list,zip(*board)))
    print(rev_board)
    if fill_row(rev_board):
        print(rev_board)
        board = rev_board
        board = list(map(list, zip(*board)))
        print(board)
        return True
    else:
        return False
        

print(fill_col(board1))
print(board1)
