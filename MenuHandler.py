import pygame

from GameConstants import GameConstants as gc

class MenuHandler:

    def menu_display_draw(self, WIN):
        pygame.font.init()
        font_welcome = pygame.font.Font("NicomediaHalftone-qZ38l.otf", 100)
        font = pygame.font.Font("Autobusbold-1ynL.ttf", 30)
        font_legend = pygame.font.SysFont("Autobusbold-1ynL.ttf", 24)
        welcome_text = font_welcome.render("NEAT PONG!", 1, gc.UI_COLOR_2)
        play_against_human_text = font.render("Human vs Human", 1, self.menu_colors()[0][0])
        play_against_neat_text = font.render("Human vs Bot", 1, self.menu_colors()[0][1])
        simulation_game_text = font.render("Human vs NEAT", 1, self.menu_colors()[0][2])
        quit_game_text = font.render("Quit game", 1, self.menu_colors()[0][3])

        
        WIN.fill(gc.BLACK)
        self.blinking_rectangle(WIN, gc.WIN_WIDTH//2 - welcome_text.get_width()//2 - 10, 150, 235, 45)
        WIN.blit(welcome_text, (gc.WIN_WIDTH//2 - welcome_text.get_width()//2, 40))
        WIN.blit(play_against_human_text, (gc.WIN_WIDTH//2 - welcome_text.get_width()//2, 160))
        WIN.blit(play_against_neat_text, (gc.WIN_WIDTH//2 - welcome_text.get_width()//2, 210))
        WIN.blit(simulation_game_text, (gc.WIN_WIDTH//2 - welcome_text.get_width()//2, 260))
        WIN.blit(quit_game_text, (gc.WIN_WIDTH//2 - welcome_text.get_width()//2, 310))
        pygame.display.update()

    def change_current_selection(self, going_down:bool):

        if going_down:
            if self.current_selection == 3:
                self.current_selection = 0
            else:
                self.current_selection += 1
        else:
            if self.current_selection == 0:
                self.current_selection = 3
            else:
                self.current_selection -= 1

    def blinking_rectangle(self, WIN, x, y, width, height):
        if self.counter > 5:
            self.counter = 0

        color = self.menu_colors()[0][self.current_selection] if self.odd_blink[self.counter] else gc.BLACK
        pygame.draw.rect(WIN, color, (x, y + self.menu_colors()[1], width, height), 3)
        self.counter += 1

    def menu_colors(self) -> tuple:
        if self.current_selection == 0:
            return (gc.UI_COLOR_6, gc.WHITE, gc.WHITE, gc.WHITE), 0
        elif self.current_selection == 1:
            return (gc.WHITE, gc.UI_COLOR_6, gc.WHITE, gc.WHITE), 50
        elif self.current_selection == 2:
            return (gc.WHITE, gc.WHITE, gc.UI_COLOR_6, gc.WHITE), 100
        elif self.current_selection == 3:
            return (gc.WHITE, gc.WHITE, gc.WHITE, gc.UI_COLOR_3), 150

    def __init__(self) -> None:
        self.current_selection = 0
        self.odd_blink = [True, True, True, False, False, False]
        self.counter = 0