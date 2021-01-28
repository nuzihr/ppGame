import pygame
from button import Button, TextButton


class BottomBar(object):
    colors = [
        (0, 0, 0),
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0),
        (255, 140, 0),
        (165, 42, 42),
        (128, 0, 128)
    ]

    def __init__(self, x, y, game, width=650, height=60):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.clear_button = TextButton(self.x + self.width - 125, self.y + 5, 100, 50, (128, 128, 128), "Clear")
        self.eraser_button = TextButton(self.x + self.width - 250, self.y + 5, 100, 50, (128, 128, 128), "Eraser")
        self.color_buttons = [
            Button(self.x+10, self.y+15, 30, 30, self.colors[0]),
            Button(self.x+50, self.y+15, 30, 30, self.colors[1]),
            Button(self.x+90, self.y+15, 30, 30, self.colors[2]),
            Button(self.x+130, self.y+15, 30, 30, self.colors[3]),
            Button(self.x+170, self.y+15, 30, 30, self.colors[4]),
            Button(self.x+210, self.y+15, 30, 30, self.colors[5]),
            Button(self.x+250, self.y+15, 30, 30, self.colors[6]),
            Button(self.x+290, self.y+15, 30, 30, self.colors[7]),
        ]

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 2)
        self.clear_button.draw(win)
        self.eraser_button.draw(win)
        for b in self.color_buttons:
            b.draw(win)

    def button_events(self):
        mouse = pygame.mouse.get_pos()
        if self.clear_button.click(*mouse):
            self.game.board.clear()
        if self.eraser_button.click(*mouse):
            self.game.draw_color = (255, 255, 255)

        for b in self.color_buttons:
            if b.click(*mouse):
                self.game.draw_color = b.color

