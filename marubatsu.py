#!/usr/bin/env python

"""
マルバツゲーム
"""
__author__  = "jabe0958"
__version__ = "0.01"
__date__    = "29 December 2017"

import numpy as np

class MaruBatsu:
    """
    マルバツゲームのクラスです。
    """

    def __init__(self, size=3):
        """
        このゲームのコンストラクタです。
        @param size 盤面のサイズ
        """

        self.size = size
        self.board = np.zeros((size, size), dtype=np.int)
        self.ongoing = True
    
    def do(self, y, x, player):
        """
        指定された座標へ着手を行います。

        @param y 縦座標
        @param x 横座標
        @param player 着手プレイヤー
        """

        if not self.ongoing:
            print("This game is over.")
            return
        if player <= 0:
            print("Player-{player} is irregular.")
            return
        if self.board[y][x] != 0:
            print("Point[{y}][{x}] is checked!".format(y=y, x=x))
            return
        else:
            self.board[y][x] = player
        self.print()
        judgement = self.judge(player)
        if judgement is None:
            print("This game is draw.")
            self.ongoing = False
        elif judgement != 0:
            print("The winner of this game is player-{player}".format(player=judgement))
            self.ongoing = False
    
    def judge(self, player):
        """
        盤面の終了評価を行います。

        @param 着手プレイヤー
        @return 評価結果 [0] 継続中 / [None] 引き分け / [左記以外] 勝利プレイヤー
        """

        for y in range(self.size):
            if np.sum(np.where(self.board[y] == player, 1, 0)) == self.size:
                return player
        for x in range(self.size): 
            if np.sum(np.where(self.board[:][x] == player, 1, 0)) == self.size:
                return player
        if np.sum(np.where(np.diag(self.board) == player, 1, 0)) == self.size:
            return player
        if np.sum(np.where(np.diag(np.fliplr(self.board)) == player, 1, 0)) == self.size:
            return player
        if np.where(self.board != 0, 1, 0).sum() == self.size * self.size:
            return None

        return 0

    def print(self):
        """
        盤面を標準出力に出力します。
        """

        for y in range(self.size):
            for x in range(self.size):
                print(self.board[y][x] , end=" ")
            print("")
        print("-----")
    
if __name__ == "__main__":
    game = MaruBatsu(size=3)
    game.do(0, 0, 1)
    game.do(0, 1, 2)
    game.do(0, 2, 2)
    game.do(1, 0, 2)
    game.do(1, 1, 1)
    game.do(1, 2, 1)
    game.do(2, 0, 1)
    game.do(2, 2, 2)
    game.do(2, 1, 1)
