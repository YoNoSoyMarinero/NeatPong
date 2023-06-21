import pygame

from GameConstants import GameConstants as gc

class Score:
    def score_display_window(self, win):
        font = pygame.font.Font("NicomediaSuperItalic-6Yavo.otf", 50)
        player_1_text = font.render(f"{self.left_score}", 1, gc.UI_COLOR_1)
        player_2_text = font.render(f"{self.right_score}", 1, gc.GRAY)
        number_of_hits = font.render(f"{self.left_hits + self.right_hits}", 1, gc.RED)
        win.blit(player_1_text, (gc.WIN_WIDTH//2 - player_1_text.get_width()//2 - 200, 40))
        win.blit(player_2_text, (gc.WIN_WIDTH//2 - player_1_text.get_width()//2 + 200, 40))
        pygame.draw.rect(win, gc.GRAY, (gc.WIN_WIDTH//2-5, 0, 5, gc.WIN_HEIGHT//3), width=5)
        pygame.draw.circle(win, gc.GRAY, (gc.WIN_WIDTH//2, gc.WIN_HEIGHT//2), gc.WIN_HEIGHT//6, width=5)
        pygame.draw.rect(win, gc.GRAY, (gc.WIN_WIDTH//2-5, 2*gc.WIN_HEIGHT//3, 5,gc.WIN_HEIGHT//3), width=5)

    def won_screen(self, win, game_mode):
        font = pygame.font.Font("NicomediaSuperItalic-6Yavo.otf", 30)
        if game_mode[0]:
            won_text_str = "Human 1 won!" if self.left_won else "Human 2 won!"
        elif game_mode[1]:
            won_text_str = "Human won!" if self.left_won else "Bot won!"
        else:
            won_text_str = "Neat won!" if self.left_won else "Human won!"
        won_text = font.render(f"{won_text_str}", 1, gc.GRAY)
        win.fill(gc.BLACK)
        win.blit(won_text, (gc.WIN_WIDTH//2 - won_text.get_width(), 220))
        pygame.display.update()
        pygame.time.wait(3000)
        self.left_won = False

    def __init__(self) -> None:
        self.left_score = 0
        self.left_hits = 0
        self.right_score = 0
        self.right_hits = 0
        self.last_scored = False
        self.left_won = False