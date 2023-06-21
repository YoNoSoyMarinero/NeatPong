import pygame
import neat
import pickle
import os

from GameConstants import GameConstants as gc
from Paddle import Paddle
from Ball import Ball
from Score import Score
from CollisonDetection import CollisonDetection
from MenuHandler import MenuHandler
from KeysHandler import KeysHandler

pygame.init()

class Game:
    def game_reset(self):
        self.fps = 10
        self.game_mode = [False, False, False]
        self.game_playing = False
        self.game_mechanics_reset()

    def game_mechanics_reset(self):
        self.score.left_score = 0
        self.score.right_score = 0
        self.score.left_hits = 0
        self.score.right_hits = 0
        self.ball.x = self.ball.original_x
        self.ball.y = self.ball.original_y
        self.paddle_left.x = self.paddle_left.x_original
        self.paddle_left.y = self.paddle_left.y_original
        self.paddle_right.x = self.paddle_right.x_original
        self.paddle_right.y = self.paddle_right.y_original

    def train_mechanics(self):
        CollisonDetection.ball_wall_collison(self.ball)
        CollisonDetection.ball_paddle_collison(self.ball,self.paddle_left, self.paddle_right, self.score)
        CollisonDetection.goal_scored(self.ball, self.score, self.paddle_left, self.paddle_right)
        self.ball.ball_movement()

    def game_mechanics(self):
        self.train_mechanics()

        if self.score.left_score == 5:
            self.score.left_won = True
            self.score.won_screen(self.WIN, self.game_mode)
            self.game_reset()
        elif self.score.right_score == 5:
            self.score.won_screen(self.WIN, self.game_mode)
            self.game_reset()

    def neat_v_human_test_ai(self, net):
        clock = pygame.time.Clock()
        self.game_playing = True
        run = True
        while run:
            clock.tick(60)
            self.display_draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                
            self.keys = pygame.key.get_pressed()

            self.keys_handler.neat_vs_human_key_handler(self)
            self.train_mechanics() 

    def neat_v_neat_train_ai(self, genome1, genome2, config):
        run = True
        self.game_playing = True
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                
            output1 = net1.activate((self.paddle_left.y, self.ball.y, abs(self.paddle_left.x - self.ball.x)))
            decision1 = output1.index(max(output1))
            output2 = net2.activate((self.paddle_left.y, self.ball.y, abs(self.paddle_left.x - self.ball.x)))
            decision2 = output2.index(max(output2))

            if decision1 == 0:
                genome1.fitness -= 0.0001
            if decision2 == 0:
                genome2.fitness -= 0.0001

            self.keys_handler.neat_vs_neat_key_handler(self, decision1, decision2)
            self.display_draw()
            self.train_mechanics()

            if self.score.left_score == 5 or self.score.right_score == 5 or self.score.left_hits > 25:
                genome1.fitness += self.score.left_hits + 10*(self.score.left_score - self.score.right_score)
                genome2.fitness += self.score.right_hits + 10*(self.score.right_score - self.score.left_score)
                self.game_mechanics_reset()
                break


    def neat_v_bot_train_ai(self, genome, config):
        run = True
        self.game_playing = True
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
        
            output = net.activate((self.paddle_left.y, self.ball.y, abs(self.paddle_left.x - self.ball.x)))
            decision = output.index(max(output))

            if decision == 0:
                genome.fitness -= 0.01

            self.keys_handler.neat_vs_bot_key_handler(self, decision)
            self.display_draw()
            self.train_mechanics()

            if self.score.left_score == 5 or self.score.right_score == 5 or self.score.left_hits > 25:
                genome.fitness += self.score.left_hits + 10*(self.score.left_score - self.score.right_score)
                self.game_mechanics_reset()
                break


    def game_display_draw(self):
        self.WIN.blit(self.field_surface, (0, 0))
        self.paddle_left.paddle_display_draw(self.WIN)
        self.paddle_right.paddle_display_draw(self.WIN)
        self.ball.ball_display_draw(self.WIN)
        self.score.score_display_window(self.WIN)
        pygame.display.update()

    def display_draw(self):
        if self.game_playing:
            self.game_display_draw()
        else:
            self.menu_handler.menu_display_draw(self.WIN)
        
    def mainloop(self):
        clock = pygame.time.Clock()
        while self.game_runing:
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_runing = False
                    break

            self.display_draw()
            self.keys = pygame.key.get_pressed()
            self.keys_handler.key_handler(self)
            if self.game_playing:
                self.game_mechanics()



    def __init__(self) -> None:
        self.WIN = pygame.display.set_mode((gc.WIN_WIDTH, gc.WIN_HEIGHT))
        self.game_runing = True
        self.game_playing = False
        self.fps = 10
        self.game_mode = [False, False, False]
        self.paddle_left = Paddle(gc.PADDLE_DISTANCE_FROM_GOAL, gc.WIN_HEIGHT//2 - gc.PADDLE_HEIGHT//2)
        self.paddle_right = Paddle(gc.WIN_WIDTH - gc.PADDLE_DISTANCE_FROM_GOAL - gc.PADDLE_WIDTH, gc.WIN_HEIGHT//2 - gc.PADDLE_HEIGHT//2)
        self.ball = Ball(gc.WIN_WIDTH//2, gc.WIN_HEIGHT//2, gc.BALL_RADIUS)
        self.score = Score()
        self.keys_handler = KeysHandler()
        self.menu_handler = MenuHandler()





        self.image = pygame.image.load("neon.jpg")
        self.field_surface = pygame.Surface((gc.WIN_WIDTH, gc.WIN_HEIGHT))
        image_x = (gc.WIN_WIDTH - self.image.get_width()) // 2
        image_y = (gc.WIN_HEIGHT - self.image.get_height()) // 2
        self.field_surface.blit(self.image, (image_x, image_y))
    

        local_dir = os.path.dirname(__file__)
        config_path = os.path.join(local_dir, "config.txt")
        self.config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation,
                            config_path)

        with open("best3.pickle", "rb") as f:
            self.winner = pickle.load(f)
        self.neat_neural_network = neat.nn.FeedForwardNetwork.create(self.winner, self.config)


        self.WIN.fill(gc.BLACK)
        pygame.display.set_caption("PONG")