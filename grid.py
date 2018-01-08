import pygame
import constant

class Grid(object):

    def __init__(self, pause):
        self.set_color(pause)

    def set_color(self, pause):
        if pause is True:
            self.color = constant.GRID_LINE_PAUSE
        else:
            self.color = constant.GRID_LINE

    def draw(self, scr):
        for i in range(1, constant.BOARD_WIDTH):
            pygame.draw.line(
                scr,
                self.color,
                [i * constant.CELL_SIZE, 0],
                [i * constant.CELL_SIZE, constant.BOARD_HEIGHT * constant.CELL_SIZE]
            )
        for j in range(1, constant.BOARD_HEIGHT):  
            pygame.draw.line(
                scr,
                self.color,
                [0, j * constant.CELL_SIZE],
                [constant.BOARD_WIDTH * constant.CELL_SIZE, j * constant.CELL_SIZE]
            )
