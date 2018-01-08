import pygame
import constant

class Board(object):

    def __init__(self):
        self.BOARD_WIDTH = constant.BOARD_WIDTH
        self.BOARD_HEIGHT = constant.BOARD_HEIGHT
        self.board = [
            [False for i in range(self.BOARD_HEIGHT)] for i in range(self.BOARD_WIDTH)
        ]

    def __iter__(self):
        for x in range(self.BOARD_WIDTH):
            for y in range(self.BOARD_HEIGHT):
                yield (x, y, self.board[x][y])

    def get_nb_neighbors(self, x, y):
        res = 0

        for i in range(9):
            if i == 4: continue
            xx = (x + (i % 3 - 1)) % self.BOARD_WIDTH
            yy = (y + (i // 3 - 1)) % self.BOARD_HEIGHT
            if self.board[xx][yy] is True:
                res += 1

        return res

    def toggle_mouse_cell(self, x, y):
        xx = int(x / constant.CELL_SIZE)
        yy = int(y / constant.CELL_SIZE)
        self.board[xx][yy] = not self.board[xx][yy]

        return self.board[xx][yy]

    def set_cell(self, x, y, value):
        self.board[x][y] = value

        return self.board[x][y]

    def draw(self, scr):
        for x, y, val in self:
            if val is True:
                pygame.draw.rect(
                    scr,
                    constant.LIVE_CELL,
                    (
                        x * constant.CELL_SIZE,
                        y * constant.CELL_SIZE,
                        constant.CELL_SIZE,
                        constant.CELL_SIZE
                    )
                )
