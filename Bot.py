import math
import random
import pygame

from GameConstants import GameConstants as gc
class Bot:
    @classmethod
    def move_paddle(cls, game):
            ranodm_miss_margin = random.randint(-50, 50)
            if game.ball.ball_velocity_x > 0:
                if game.ball.y < game.paddle_right.y + gc.PADDLE_HEIGHT//2 + ranodm_miss_margin:
                    game.paddle_right.paddle_move(True)
                elif game.ball.y > game.paddle_right.y - gc.PADDLE_HEIGHT//2 + ranodm_miss_margin:
                    game.paddle_right.paddle_move(False)
                else:
                    pass
            else:
                if gc.WIN_HEIGHT//2 < game.paddle_right.y + gc.PADDLE_HEIGHT//2:
                     game.paddle_right.paddle_move(True)
                elif gc.WIN_HEIGHT//2 > game.paddle_right.y - gc.PADDLE_HEIGHT//2:
                     game.paddle_right.paddle_move(False)


