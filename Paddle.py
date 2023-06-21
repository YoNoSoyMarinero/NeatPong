import pygame
from GameConstants import GameConstants as gc

class Paddle:

    def paddle_display_draw(self, win):
        pygame.draw.rect(win, self.PADDLE_COLOR, (self.x, self.y, self.width, self.height))

    def paddle_move(self, up:bool):
            if up:
                if self.y > 0:
                    self.y -= self.PADDLE_VELOCITY
            else:
                if self.y + self.PADDLE_VELOCITY + self.height <= gc.WIN_HEIGHT:
                    self.y += self.PADDLE_VELOCITY

    def __init__(self, x, y) -> None:
        self.PADDLE_COLOR = gc.WHITE
        self.PADDLE_VELOCITY = gc.PADDLE_VELOCITY
        self.width = gc.PADDLE_WIDTH
        self.height = gc.PADDLE_HEIGHT


        self.x = self.x_original = x;
        self.y = self.y_original = y;