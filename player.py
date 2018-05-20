import numpy as np
import game

class Player:

    def __init__(self, identifier):
        self.identifier = identifier

class FixedPlayer(Player):
    ''' Plays fixed move in a given state '''
    
    def __init__(self, identifier):
        self.moves = {}
        self.identifier = identifier
        
        # Iterate all possible boards, and pick a random move for that board
        boards = []
        generate_boards(np.zeros(9).astype("int8"), boards, 0)
        
        for board in boards:
            legal_moves = game.legal(board)
            
            if len(legal_moves) == 0:
                continue

            move = np.random.choice(legal_moves, 1)[0]
            
            self.moves[game.board2str(board)] = move

    def move(self, board, legal_moves):
        return self.moves[game.board2str(board)]

class RandomPlayer(Player):
    ''' Plays a random legal move, uniformly, every time '''

    def __init__(self, identifier):
        self.identifier = identifier

    def move(self, board, legal_moves):
        return np.random.choice(np.where(legal_moves == 0)[0], 1)[0]
        
class TempDiffPlayer:

    def __init__(self):
        self.value = dict()

def generate_boards(board, boards, index):
    if index == 9:
        boards.append(board)
        return

    for i in [1, -1, 0]:
        board[index] = i
        generate_boards(board.copy(), boards, index+1)

