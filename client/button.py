import pygame


class Button:

    def __init__(self, x, y, width, height, color, boarder_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.boarder_color = boarder_color
        self.BOARDER_WIDTH = 2

    def draw(self, win):
        pygame.draw.rect(win, self.boarder_color, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(
            win,
            self.color,
            (self.x + self.BOARDER_WIDTH,
             self.y + self.BOARDER_WIDTH,
             self.width - self.BOARDER_WIDTH * 2,
             self.height - self.BOARDER_WIDTH * 2),
            0)

    def click(self, x, y):
        """

        :param x: float
        :param y: float
        :return: bool
        """
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class TextButton(Button):

    def __init__(self, x, y, width, height, color, text):
        super().__init__(x, y, width, height, color)
        self.text = text
        self.text_font = pygame.font.SysFont("comicsans", 30)

    def change_font_size(self, size):
        self.text_font = pygame.font.SysFont("comicsans", size)

    def draw(self, win):
        super().draw(win)
        text = self.text_font.render(self.text, True, (0, 0, 0))
        win.blit(text, (self.x+self.width/2 - text.get_width()/2,
                        self.y+self.height/2 - text.get_height()/2))


class ColorButton(object):

    def __init__(self):
        pass
