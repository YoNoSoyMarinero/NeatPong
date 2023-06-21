import pygame

from Bot import Bot

class KeysHandler:

    def neat_vs_neat_key_handler(self, game, decision1, decision2):
        if decision1 == 1:
            game.paddle_left.paddle_move(True)
        elif decision2 == 2:
            game.paddle_left.paddle_move(False)
        if decision2 == 1:
            game.paddle_right.paddle_move(True)
        elif decision2 == 2:
            game.paddle_right.paddle_move(False)

    def neat_vs_human_key_handler(self, game):
        output = game.neat_neural_network.activate((game.paddle_left.y, game.ball.y, abs(game.paddle_left.x - game.ball.x)))
        decision = output.index(max(output))

        if game.keys[pygame.K_ESCAPE]:
            game.game_playing = False
            game.game_reset()

        if decision == 1:
            game.paddle_left.paddle_move(True)
        elif decision == 2:
            game.paddle_left.paddle_move(False)
            
        if game.keys[pygame.K_UP]:
            game.paddle_right.paddle_move(True)
        if game.keys[pygame.K_DOWN]:
            game.paddle_right.paddle_move(False)


    def neat_vs_bot_key_handler(self, game, decision):
        if game.keys[pygame.K_ESCAPE]:
            game.game_playing = False
            game.game_reset()

        if decision == 1:
            game.paddle_left.paddle_move(True)
        elif decision == 2:
            game.paddle_left.paddle_move(False)

        Bot.move_paddle(game)


    def human_vs_bot_key_handler(self, game):
        if game.keys[pygame.K_ESCAPE]:
            game.game_playing = False
            game.game_reset()

        if game.keys[pygame.K_w]:
            game.paddle_left.paddle_move(True)
        if game.keys[pygame.K_s]:
            game.paddle_left.paddle_move(False)

        Bot.move_paddle(game)


    def human_vs_human_key_handler(self, game):
        if game.keys[pygame.K_ESCAPE]:
            game.game_playing = False
            game.game_reset()

        if game.keys[pygame.K_w]:
            game.paddle_left.paddle_move(True)
        if game.keys[pygame.K_s]:
            game.paddle_left.paddle_move(False)

        if game.keys[pygame.K_UP]:
            game.paddle_right.paddle_move(True)
        if game.keys[pygame.K_DOWN]:
            game.paddle_right.paddle_move(False)

    def menu_keys_handler(self, game):
        if game.keys[pygame.K_RETURN]:
            if game.menu_handler.current_selection == 3:
                pygame.quit()
                game.game_runing = False
            else:
                game.fps = 60
                game.game_mode[game.menu_handler.current_selection] = True
                game.game_playing = True
        if game.keys[pygame.K_DOWN]:
            game.menu_handler.change_current_selection(True)
            game.game_running = True
        elif game.keys[pygame.K_UP]:
            game.menu_handler.change_current_selection(False)
            game.game_running = True
        else:
            game.game_running = True

    def key_handler(self, game):
        if game.game_playing:
            if game.game_mode[0]:
                self.human_vs_human_key_handler(game)
            elif game.game_mode[1]:
                self.human_vs_bot_key_handler(game)
            elif game.game_mode[2]:
                self.neat_vs_human_key_handler(game)
        else:
            self.menu_keys_handler(game)