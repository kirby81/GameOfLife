import pygame
import constant
from pygame.locals import *
from board import Board
from grid import Grid

class GameOfLife(object):

    def __init__(self):
        pygame.init()

        self.pause = True
        self.evolution = 0
        self.fps_cap = pygame.time.Clock()
        self.screen = pygame.display.set_mode((
            constant.BOARD_WIDTH * constant.CELL_SIZE,
            constant.BOARD_HEIGHT * constant.CELL_SIZE
        ))
        self.board = Board()
        self.grid = Grid(self.pause)
        self.game_loop()

    def game_loop(self):
        while True:
            self.fps_cap.tick(constant.FPS_CAP)
            self.process_event()
            self.draw()
            if self.pause is False:
                self.compute_next_evolution()

    def draw(self):
        self.screen.fill(constant.DEAD_CELL)
        self.board.draw(self.screen)
        self.grid.draw(self.screen)
        pygame.display.update()

    def process_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.toggle_pause()
                elif event.key == K_ESCAPE:
                    exit()
            if event.type == MOUSEBUTTONDOWN and self.pause is True:
                x, y = pygame.mouse.get_pos()
                self.board.toggle_mouse_cell(x, y)


    def toggle_pause(self):
        self.pause = not self.pause
        self.grid.set_color(self.pause)

    def compute_next_evolution(self):
        new_board = Board()

        for x, y, val in self.board:
            nb_neighbor = self.board.get_nb_neighbors(x, y)
            if (nb_neighbor == 3) or ((val is True) and (nb_neighbor == 2)):
                new_board.set_cell(x, y, True)
            else:
                new_board.set_cell(x, y, False)

        self.board = new_board
        self.evolution += 1
