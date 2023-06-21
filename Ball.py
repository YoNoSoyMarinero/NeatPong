import math
import pygame
import random

from GameConstants import GameConstants as gc

class Ball:
    
    def set_speed(self, left_paddle, right_paddle, right_paddle_hit):
        if right_paddle_hit:
            ball_paddle_center_distance = self.y - (right_paddle.y - right_paddle.height//2) - right_paddle.height
            if ball_paddle_center_distance <= 0:
                deflection_angle = math.pi*((ball_paddle_center_distance + 60)/120 + 3/2)
                deflection_angle = deflection_angle if deflection_angle > 14*math.pi/8 else 14*math.pi/8
                self.ball_velocity_x = -self.ball_speed*math.cos(deflection_angle)
                self.ball_velocity_y = self.ball_speed*math.sin(deflection_angle)
            else:
                deflection_angle = math.pi*(ball_paddle_center_distance/-120 + 1)
                deflection_angle = deflection_angle if deflection_angle < 6*math.pi/8 else 6*math.pi/8
                self.ball_velocity_x = self.ball_speed*math.cos(deflection_angle)
                self.ball_velocity_y = self.ball_speed*math.sin(deflection_angle)
            
        else:
            ball_paddle_center_distance = self.y - (left_paddle.y - left_paddle.height//2) - right_paddle.height
            if ball_paddle_center_distance <= 0:
                deflection_angle = math.pi*((ball_paddle_center_distance + 60)/120 + 3/2)
                deflection_angle = deflection_angle if deflection_angle > 14*math.pi/8 else 14*math.pi/8
                self.ball_velocity_x = self.ball_speed*math.cos(deflection_angle)
                self.ball_velocity_y = self.ball_speed*math.sin(deflection_angle)
            else:
                deflection_angle = math.pi*(ball_paddle_center_distance/-120 + 1)
                deflection_angle = deflection_angle if deflection_angle < 6*math.pi/8 else 6*math.pi/8
                self.ball_velocity_x = -self.ball_speed*math.cos(deflection_angle)
                self.ball_velocity_y = self.ball_speed*math.sin(deflection_angle)


    def ball_movement(self):
        self.x += self.ball_velocity_x
        self.y += self.ball_velocity_y

    def ball_display_draw(self, win):
        pygame.draw.circle(win, (random.randint(0,255), random.randint(0,255),random.randint(0,255)) , (self.x, self.y), self.radius)

    def __init__(self, x, y, radius) -> None:
        random_angle = random.uniform(46*math.pi/24 , 50*math.pi/24)
        direction = 1 if random.random() > 0.5 else -1
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.ball_speed = gc.BALL_VELOCITY
        self.ball_velocity_x = direction*self.ball_speed*math.cos(random_angle)
        self.ball_velocity_y = self.ball_speed*math.sin(random_angle)
        self.radius = radius