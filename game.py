import numpy as np
import player

class Game:
    def __init__(self):
        self.board = np.zeros((3, 3)).astype("int8")
        self.legal = np.zeros(9).astype("bool")

    def play(self, move: int, player: player.Player):
        x = move // 3
        y = move % 3

        if self.board[x, y] != 0:
            raise ValueError("Illegal position")

        self.board[x, y] = player.identifier
        self.legal[move] = 1

    def over(self) -> int:
        for row in self.board:
            res = _win_helper(row.sum())
            if res != 0: return res
        
        for col in self.board.T:
            res = _win_helper(col.sum())
            if res != 0: return res

        diag = _win_helper(self.board[0, 0] + self.board[1, 1] + self.board[2, 2])
        diag2 = _win_helper(self.board[0, 2] + self.board[1, 1] + self.board[2, 0])

        if diag != 0: return diag
        
        return diag2

def _win_helper(result):
    if result == 3:
        return 1 # Player 1 won
    if result == -3:
        return -1 # Player 2 won
    return 0 # Inconclusive

def board2str(board):
    return "".join([str(x) for x in board.flatten()])

def str2board(string):
    return np.array([int(x) for x in string]).reshape(3, 3).astype("int8")

def legal(board):
    return np.where(board.flatten() == 0)[0]
