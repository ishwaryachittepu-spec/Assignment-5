import random
import copy

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

    def winner(self):

        wins = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]

        for win in wins:

            a, b, c = win

            if self.board[a] == self.board[b] == self.board[c] != EMPTY:
                return self.board[a]

        if EMPTY not in self.board:
            return "Draw"

        return None


def random_playout(game, current_player):

    while game.winner() is None:

        move = random.choice(game.available_moves())

        game.make_move(move, current_player)

        if current_player == PLAYER_X:
            current_player = PLAYER_O
        else:
            current_player = PLAYER_X

    return game.winner()


def mcts(game, simulations, player):

    move_scores = {}

    for move in game.available_moves():

        wins = 0

        for _ in range(simulations):

            temp_game = copy.deepcopy(game)

            temp_game.make_move(move, player)

            next_player = PLAYER_O if player == PLAYER_X else PLAYER_X

            result = random_playout(temp_game, next_player)

            if result == player:
                wins += 1

        move_scores[move] = wins

    best_move = max(move_scores, key=move_scores.get)

    return best_move


game = TicTacToe()

game.board = [
    'X', 'X', ' ',
    'O', 'O', ' ',
    ' ', ' ', ' '
]

game.print_board()

move = mcts(game, 1000, PLAYER_X)

print("\nBest Move =", move)
