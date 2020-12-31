# from IPython.display import clear_output


def display_board(board):   
    print('   |   |   ')
    # print(f' {board[7]} | {board[8]} | {board[9]}'.format(board[7],board[8],board[9]))
    print(' {} | {} | {}'.format(board[7],board[8],board[9]))
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    # print(f' {board[4]} | {board[5]} | {board[6]}')
    print(' {} | {} | {}'.format(board[4],board[5],board[6]))
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    # print(f' {board[1]} | {board[2]} | {board[3]}')
    print(' {} | {} | {}'.format(board[1],board[2],board[3]))
    print('   |   |   ')

def player_input(board,player1):
    move = 0
    if player1 == True:
        print('Player 1')
    else:
        print('Player 2')
    while move not in range(1,10):
        move = int(input('Where would you like to move? (1-9)'))
        if move not in range(1,10):
            print('Please pick a valid space number! (1-9)')
        if board[move] != ' ':
            print('This space is taken! Pick another space.')
            move = 0
    return move

def make_move(board,piece,move):
    board[move] = piece
    return board
    
def reset_board():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    return board

def alternate_move(piece):
    if piece == 'X':
        piece = 'O'
    else:
        piece = 'X'
    return piece

def winner_check(board):
    if ''.join([board[1],board[2],board[3]]) == 'XXX' or ''.join([board[4],board[5],board[6]]) == 'XXX' or ''.join([board[7],board[8],board[9]]) == 'XXX' or ''.join([board[1],board[4],board[7]]) == 'XXX' or ''.join([board[2],board[5],board[8]]) == 'XXX' or ''.join([board[3],board[6],board[9]]) == 'XXX' or ''.join([board[1],board[5],board[9]]) == 'XXX' or ''.join([board[3],board[5],board[9]]) == 'XXX':
        return 'X'
    elif ''.join([board[1],board[2],board[3]]) == 'OOO' or ''.join([board[4],board[5],board[6]]) == 'OOO' or ''.join([board[7],board[8],board[9]]) == 'OOO' or ''.join([board[1],board[4],board[7]]) == 'OOO' or ''.join([board[2],board[5],board[8]]) == 'OOO' or ''.join([board[3],board[6],board[9]]) == 'OOO' or ''.join([board[1],board[5],board[9]]) == 'OOO' or ''.join([board[3],board[5],board[9]]) == 'OOO':
        return 'O'
    elif board.count(' ') == 1:
        return 'tie'
    else:
        pass

def tie_check(board):
    if board.count(' ') == 1:
        gameover = True
        return 'tie'
    else:
        pass

def gameover_check(winner):
    if winner == 'X' or winner == 'tie' or winner == 'O':
        return True
    else:
        return False

def choose_piece():
    chosen = False
    while chosen == False:
        piece = input('Player1, do you want to be X or O? (X or O)')
        if piece == 'X' or piece =='O':
            chosen = True
            return piece
        else:
            print('Please choose a valid piece! (X or O)')
            
def choose_player():
    import random
    flip = random.randint(0,1)
    if flip == 0:
        return True
    else:
        return False

def play_again():
    play = ''
    while play != 'Y' or play != 'X':
        play = input('Play again? ')
        if play == 'Y':
            return True
        elif play == 'N':
            return False
        else:
            print('Please type Y or N')

def declare_winner(winner):
    if winner == 'tie':
        print('This game is a tie.')
    elif player1 == True:
        print('Player 2 wins!')
    else:
        print('Player 1 wins!')

if __name__ == "__main__":
    active = True
    while active == True:
        gameover = False
        board = reset_board()
        print('Welcome to Tic-Tac-Toe')
        piece = choose_piece()
        player1 = choose_player()
        while gameover == False:
            clear_output()
            display_board(board)
            move = player_input(board,player1)
            make_move(board,piece,move)
            piece = alternate_move(piece)
            winner = winner_check(board)
            gameover = gameover_check(winner)
            player1 = not player1
        clear_output()
        display_board(board)
        declare_winner(winner)
        active = play_again()
        clear_output()

