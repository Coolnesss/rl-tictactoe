from game import Game
from player import RandomPlayer, FixedPlayer, TempDiffPlayer
import numpy as np

def play_game_test():
    n_games = 10000
    winners = np.zeros(n_games)

    ''' Play 1000 random games '''
    p1 = RandomPlayer(1)
    p2 = RandomPlayer(-1)
    for idx in range(n_games):
        g = Game()

        order = [p1, p2, p1, p2, p1, p2, p1, p2, p1]

        for player in order:
            g.play(player.move(g.board, g.legal), player)

            if g.over():
                break

        winners[idx] = g.over()
    
    p1_won = (winners == 1).sum()
    p2_won = (winners == -1).sum()
    draws = n_games - p1_won - p2_won

    print(f"Player 1 won [{p1_won}] times, player 2 [{p2_won}] times, and [{draws}] draws")


def play_fixed_test():
    n_games = 1000
    winners = np.zeros(n_games)

    ''' Play 1000 random games '''
    p1 = FixedPlayer(1)
    p2 = RandomPlayer(-1)
    for idx in range(n_games):
        g = Game()

        order = [p1, p2, p1, p2, p1, p2, p1, p2, p1]

        for player in order:
            g.play(player.move(g.board, g.legal), player)

            if g.over():
                break

        winners[idx] = g.over()
    
    p1_won = (winners == 1).sum()
    p2_won = (winners == -1).sum()
    draws = n_games - p1_won - p2_won

    print(f"Player 1 won [{p1_won}] times, player 2 [{p2_won}] times, and [{draws}] draws")

if __name__ == '__main__':
    #play_game_test()
    play_fixed_test()