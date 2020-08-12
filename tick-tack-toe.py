empt_board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}

board_keys = []

for key in empt_board:
    board_keys.append(key)

def opt_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-*-*-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-*-*-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def tick_tack_toe():
    turn = 'X'
    count = 0

    for i in range(10):
        opt_board(empt_board)
        print("your turn [" + turn + "] .move?")
        move = input()

        if empt_board[move] == ' ':
            empt_board[move] = turn
            count += 1
        else:
            print("Position Taken!. move?")
            continue
        
        if count >= 5:
            if empt_board['7'] == empt_board['8'] == empt_board['9'] != ' ': # across the top
                opt_board(empt_board)
                print("\nThe End!\n")                
                print(turn + " Wins!")                
                break
            elif empt_board['4'] == empt_board['5'] == empt_board['6'] != ' ': # across the middle
                opt_board(empt_board)
                print("\nThe End!\n")                
                print(turn + " Wins!")  
                break
            elif empt_board['1'] == empt_board['2'] == empt_board['3'] != ' ': # across the bottom
                opt_board(empt_board)
                print("\nThe End!\n")                
                print(turn + " Wins!")  
                break
            elif empt_board['1'] == empt_board['4'] == empt_board['7'] != ' ': # down the left side
                opt_board(empt_board)
                print("\nThe End!\n")                
                print(turn + " Wins!")  
                break
            elif empt_board['2'] == empt_board['5'] == empt_board['8'] != ' ': # down the middle
                opt_board(empt_board)
                print("\nThe End!\n")                
                print(turn + " Wins!")  
                break
            elif empt_board['3'] == empt_board['6'] == empt_board['9'] != ' ': # down the right side
                opt_board(empt_board)
                print("\nThe End!\n")                
                print(turn + " Wins!")  
                break 
            elif empt_board['7'] == empt_board['5'] == empt_board['3'] != ' ': # diagonal
                opt_board(empt_board)
                print("\nThe End!\n")                
                print(turn + " Wins!")  
                break
            elif empt_board['1'] == empt_board['5'] == empt_board['9'] != ' ': # diagonal
                opt_board(empt_board)
                print("\nThe End!\n")                
                print(turn + " Wins!")  
                break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
        if count == 9:
            print("\n***** Game Over. Its a Tie! *****\n")
            print(i)
    
    restart = input("Play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            empt_board[key] = " "
        tick_tack_toe()
    else:
        exit()

if __name__ == "__main__":
    tick_tack_toe()