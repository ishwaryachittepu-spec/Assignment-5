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


def heuristic(game):

    lines = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    score = 0

    for line in lines:

        values = [game.board[i] for i in line]

        if values.count(PLAYER_X) == 2 and values.count(EMPTY) == 1:
            score += 5

        if values.count(PLAYER_O) == 2 and values.count(EMPTY) == 1:
            score -= 5

    return score


def heuristic_alpha_beta(game, depth, alpha, beta,
                         is_maximizing, max_depth):

    result = game.winner()

    if result == PLAYER_X:
        return 100

    elif result == PLAYER_O:
        return -100

    elif result == "Draw":
        return 0

    if depth == max_depth:
        return heuristic(game)

    if is_maximizing:

        best_score = -math.inf

        for move in game.available_moves():

            game.make_move(move, PLAYER_X)

            score = heuristic_alpha_beta(
                game,
                depth + 1,
                alpha,
                beta,
                False,
                max_depth
            )

            game.undo_move(move)

            best_score = max(best_score, score)

            alpha = max(alpha, best_score)

            if alpha >= beta:
                break

        return best_score

    else:

        best_score = math.inf

        for move in game.available_moves():

            game.make_move(move, PLAYER_O)

            score = heuristic_alpha_beta(
                game,
                depth + 1,
                alpha,
                beta,
                True,
                max_depth
            )

            game.undo_move(move)

            best_score = min(best_score, score)

            beta = min(beta, best_score)

            if alpha >= beta:
                break

        return best_score


def best_move(game):

    best_score = -math.inf
    move_choice = None

    for move in game.available_moves():

        game.make_move(move, PLAYER_X)

        score = heuristic_alpha_beta(
            game,
            0,
            -math.inf,
            math.inf,
            False,
            3
        )

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
