import pygame
from button import Button, TextButton
from board import Board
from top_bar import TopBar
from tool_bar import ToolBar
from menu import Menu
from main_menu import MainMenu
from leaderboard import Leaderboard
from player import Player


class Game(object):
    BG = (255, 255, 255)

    def __init__(self):
        self.height = 900
        self.width = 1200
        self.win = pygame.display.set_mode((self.width, self.height))
        self.leaderboard = Leaderboard(20, 120)
        self.board = Board(250, 120)
        self.top_bar = TopBar(10, 10, 1180, 100)
        self.top_bar.change_round(1)
        self.players = [Player("Tim"),
                        Player("John"),
                        Player("Bill"),
                        Player("Joe"),
                        Player("Jeff")]
        self.skip_button = TextButton(50, 750, 150, 50, (250, 250, 0), "Skip")
        for p in self.players:
            self.leaderboard.add_player(p)

    def draw(self):
        self.win.fill(self.BG)
        self.leaderboard.draw(self.win)
        self.top_bar.draw(self.win)
        self.board.draw(self.win)
        self.skip_button.draw(self.win)
        pygame.display.update()

    def check_click(self):
        mouse = pygame.mouse.get_pos()

        if self.skip_button.click(*mouse):
            print("Click")

        clicked_board = self.board.click(*mouse)
        if clicked_board:
            self.board.update(*clicked_board, (100, 100, 100))

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
        pygame.quit()


if __name__ == "__main__":
    pygame.font.init()
    g = Game()
    g.run()
