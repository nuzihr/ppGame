import pygame
from button import Button, TextButton
from board import Board
from top_bar import TopBar
from main_menu import MainMenu
from chat import Chat
from leaderboard import Leaderboard
from player import Player
from bottom_bar import BottomBar


class Game(object):
    BG = (255, 255, 255)

    def __init__(self):
        self.height = 900
        self.width = 1200
        self.win = pygame.display.set_mode((self.width, self.height))
        self.leaderboard = Leaderboard(20, 120)
        self.board = Board(250, 120)
        self.top_bar = TopBar(10, 10, 1180, 100)
        self.draw_color = (0, 0, 0)
        self.top_bar.change_round(1)
        self.players = [Player("Tim"),
                        Player("John"),
                        Player("Bill"),
                        Player("Joe"),
                        Player("Jeff")]
        self.skip_button = TextButton(50, 785, 150, 50, (250, 250, 0), "Skip")
        self.bottom_bar = BottomBar(250, 780, self)
        self.chat = Chat(925, 120)
        for p in self.players:
            self.leaderboard.add_player(p)

    def draw(self):
        self.win.fill(self.BG)
        self.leaderboard.draw(self.win)
        self.top_bar.draw(self.win)
        self.board.draw(self.win)
        self.skip_button.draw(self.win)
        self.bottom_bar.draw(self.win)
        self.chat.draw(self.win)
        pygame.display.update()

    def check_click(self):
        mouse = pygame.mouse.get_pos()

        if self.skip_button.click(*mouse):
            print("Click")

        clicked_board = self.board.click(*mouse)
        if clicked_board:
            self.board.update(*clicked_board, self.draw_color)

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(200)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if pygame.mouse.get_pressed()[0]:
                    self.check_click()
                    self.bottom_bar.button_events()
                if event.type == pygame.KEYDOWN:
                    key_name = pygame.key.name(event.key)
                    key_name = key_name.upper()
                    self.chat.type(key_name)
        pygame.quit()


if __name__ == "__main__":
    pygame.font.init()
    g = Game()
    g.run()
