import math

EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

class TicTacToe:

    def __init__(self):
        self.board = [EMPTY] * 9

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i:i+3])

    def available_moves(self):
        return [i for i in range(9) if self.board[i] == EMPTY]

    def make_move(self, position, player):
        self.board[position] = player

    def undo_move(self, position):
        self.board[position] = EMPTY

    def winner(self):

        win_positions = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]

        for pos in win_positions:
            a, b, c = pos

            if self.board[a] == self.board[b] == self.board[c] != EMPTY:
                return self.board[a]

        if EMPTY not in self.board:
            return "Draw"

        return None


def minimax(game, is_maximizing):

    result = game.winner()

    if result == PLAYER_X:
        return 1

    elif result == PLAYER_O:
        return -1

    elif result == "Draw":
        return 0

    if is_maximizing:

        best_score = -math.inf

        for move in game.available_moves():

            game.make_move(move, PLAYER_X)

            score = minimax(game, False)

            game.undo_move(move)

            best_score = max(best_score, score)

        return best_score

    else:

        best_score = math.inf

        for move in game.available_moves():

            game.make_move(move, PLAYER_O)

            score = minimax(game, True)

            game.undo_move(move)

            best_score = min(best_score, score)

        return best_score


def best_move(game):

    best_score = -math.inf
    move_choice = None

    for move in game.available_moves():

        game.make_move(move, PLAYER_X)

        score = minimax(game, False)

        game.undo_move(move)

        if score > best_score:
            best_score = score
            move_choice = move

    return move_choice


game = TicTacToe()

game.board = [
    'X', 'X', ' ',
    'O', 'O', ' ',
    ' ', ' ', ' '
]

game.print_board()

move = best_move(game)

print("\nBest Move =", move)
