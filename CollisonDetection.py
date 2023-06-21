import math
import random
import pygame

from Ball import Ball
from Score import Score
from Paddle import Paddle
from GameConstants import GameConstants as gc


class CollisonDetection:
    @classmethod
    def goal_scored(cls, ball:Ball, score:Score, paddle_left:Paddle, paddle_right:Paddle):
        random_angle = random.uniform(46*math.pi/24 , 50*math.pi/24)
        direction = 1 if random.random() > 0.5 else -1
        if ball.x < paddle_left.x + paddle_left.width:
            score.right_score += 1
            score.left_hits = 0
            score.right_hits = 0
            ball.ball_velocity_x = direction*ball.ball_speed*math.cos(random_angle)
            ball.ball_velocity_y = ball.ball_speed*math.sin(random_angle)
            ball.x = ball.original_x
            ball.y = ball.original_y
            paddle_left.x = paddle_left.x_original
            paddle_left.y = paddle_left.y_original
            paddle_right.x = paddle_right.x_original
            paddle_right.y = paddle_right.y_original
            pygame.time.wait(1000)
        elif ball.x > gc.WIN_WIDTH - paddle_left.x - paddle_right.width:
            score.left_score += 1
            score.left_hits = 0
            score.right_hits = 0
            ball.ball_velocity_x = direction*ball.ball_speed*math.cos(random_angle)
            ball.ball_velocity_y = ball.ball_speed*math.sin(random_angle)
            ball.x = ball.original_x
            ball.y = ball.original_y
            paddle_left.x = paddle_left.x_original
            paddle_left.y = paddle_left.y_original
            paddle_right.x = paddle_right.x_original
            paddle_right.y = paddle_right.y_original
            pygame.time.wait(1000)

        


    @classmethod
    def ball_paddle_collison(cls, ball:Ball, left_paddle:Paddle, right_paddle:Paddle, score: Score):
        if ball.ball_velocity_x > 0 and ball.x + ball.radius >= right_paddle.x and ball.y >= right_paddle.y - ball.radius and ball.y <=  right_paddle.y + right_paddle.height + ball.radius//2:
            ball.set_speed(left_paddle, right_paddle, True)
            score.right_hits += 1
        elif ball.ball_velocity_x < 0 and ball.x - ball.radius <= left_paddle.x  + left_paddle.width and ball.y >= left_paddle.y - ball.radius and ball.y <= left_paddle.height + left_paddle.y + ball.radius//2:
            ball.set_speed(left_paddle, right_paddle, False)
            score.left_hits += 1

    @classmethod
    def ball_wall_collison(cls, ball: Ball):
        if ball.y - ball.radius <= 0 and ball.ball_velocity_y < 0: 
            ball.ball_velocity_y *= -1
        elif ball.y + ball.radius >= gc.WIN_HEIGHT and ball.ball_velocity_y > 0:
            ball.ball_velocity_y *= -1