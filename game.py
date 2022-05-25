import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        #getting rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|'+'|'.join(row)+'|')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'+'|'.join(row)+'|')

    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == " " ]
        # moves=[]
        # for(i, spot) in enumerate(self.board):
        #     if spot==" ":
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board
    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move then make the move i.e assign square to letter, return True
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #3 in a row

        #check row
        row_index = square//3
        row = self.board[row_index*3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        #check column    
        col_index = square % 3
        column = [self.board[col_index*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagnols -- 0,2,4,6,8 dig1-- 0,4,8 dig2 -- 2,4,6
        if square%2==0:
            dig1 = [self.board[i] for i in [0,4,8]]
            if all([spot==letter for spot in dig1]):
                return True
            dig2 = [self.board[i] for i in [2,4,6]]
            if all([spot==letter for spot in dig2]):
                return True

        #if all fails, 
        return False



def play(game, x_player, o_player, print_game = True):
    #returns winner if there is a one otherwise none - tie,
    if print_game:
        game.print_board_nums()

    letter = "X" # start letter
    #iterate while the game still has empty squares

    while game.empty_squares():
        #get the move from appropriate player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #function for move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print("")
            if game.current_winner:
                if print_game:
                    print(letter+' wins !')
                return letter
            letter = "O" if letter == "X" else "X"
        time.sleep(0.8)
    if print_game:
        print('It\'s a tie')


