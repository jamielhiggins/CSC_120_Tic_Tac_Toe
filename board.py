board1 = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]



def print_board():
    for row in board1:
        print(row)


def place_mark():
    print_board()

    #player_turn()


def player_turn():
    move = input("Enter you selection : ")
    move = int(move)

    for i in board1:
        if board1[move] == len(board1):
            board1[move] = 'X'
    print_board()


#            len(board1) == move:
 #           board1[] = 'X'
 #       elif len(board1) == 'O':
 #           print("Invalid move")
 #           continue


place_mark()
