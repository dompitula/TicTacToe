import pygame
from const import *
from board import Board

class Game:

    def __init__(self):
        self.board = Board()
        self.player = 1
        self.playing = True
        pygame.font.init()

    def render_board(self, surface):
        self.board.render(surface)

    def next_turn(self):
        self.player = 2 if self.player == 1 else 1

    def ultimate_winner(self, surface, winner):
        print("Winner! ->", winner)

        if winner == 1:
            color = CROSS_COLOR

            iDesc = (WIDTH // 2 - 110, HEIGHT // 2 - 110)
            fDesc = (WIDTH // 2 + 110, HEIGHT // 2 + 110)
            iAsc = (WIDTH // 2 - 110, HEIGHT // 2 + 110)
            fAsc = (WIDTH // 2 + 110, HEIGHT // 2 - 110)

            pygame.draw.line(surface, color, iDesc, fDesc, 22)
            pygame.draw.line(surface, color, iAsc, fAsc, 22)

        else:
            color = CIRCLE_COLOR
            center = (WIDTH // 2, HEIGHT // 2)
            pygame.draw.circle(surface, color, center, WIDTH // 4, 22)

        font = pygame.font.SysFont("monospace", 64)
        label = font.render("WON!", 1, color)
        surface.blit(label, (WIDTH // 2 - label.get_rect().width // 2, HEIGHT // 2 + 220))

        self.playing = False

    def restart(self):
        self.__init__()