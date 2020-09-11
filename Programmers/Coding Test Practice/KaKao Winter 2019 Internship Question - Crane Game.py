# 2019 Winter Kakao Winter Internship problem
# 코딩테스트 연습
# 2019 카카오 개발자 겨울 인턴십
# 크레인 인형뽑기 게임

# Crane Problem

# Programmer : CJ Jang

# the function is given n by n "board" and a series of "moves".
# the "dolls" are number between 1~100 and they are stacked on the n by n board.
# the preoccupied space will be assigned by those dolls (number 1 ~ 100)
# unoccupied space is expressed as 0.

# The series of "moves" will move the doll from board to stack.
# if there are two consecutive same items, they get "popped" and you need to count
# the number of dolls that have been "popped".

def solution(board, moves):
    answer = 0
    board_size = len(board) #board_size can be dynamically change
    temp_board = board #temp variable for board
    stack = [] #create empty stack
    
    
    for i in moves: # this for loop decides which column of the board I should look for the dolls
        
        for j in range(0,board_size): # go through all rows of the board
            if temp_board[j][i-1] != 0: # if current row at move_col is preoccupied
                stack.append(temp_board[j][i-1]) # push that doll into your stack
                temp_board[j][i-1] = 0 # remove the doll from the board
                
                if len(stack)>1 and stack[len(stack)-1] == stack[len(stack)-2] : 
                    # if the stack length is equal or longer than 2  AND two last consecutive items are the same/                       # pop those puppies away from our stack
                    stack.pop()
                    stack.pop()
                    answer += 2  # add the number of "popped" dolls
                break  # we reached the space where the space is occupied by a doll, so move onto another move.
    return answer # return answer.
    
    
   # tested by Progammers, got accepted by all test cases.
print(solution([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0]],[1, 2, 3, 3, 2, 3, 1])) # should return 4

#
