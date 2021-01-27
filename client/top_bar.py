import pygame


class TopBar(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.word = ""
        self.round = 1
        self.max_round = 8
        self.round_font = pygame.font.SysFont("comicsans", 50)
        self.BOARDER_THICKNESS = 5

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), self.BOARDER_THICKNESS)
        text = self.round_font.render("Round {} of {}".format(self.round, self.max_round), True, (0, 0, 0))
        win.blit(text, (self.x+10, self.y+self.height/2-text.get_height()/2))

        text = self.round_font.render(TopBar.underscore_text(self.word), True, (0, 0, 0))
        win.blit(text, (self.x + self.width/2 - text.get_width()/2,
                        self.y + self.height/2 - text.get_height()/2 + 10))

    @staticmethod
    def underscore_text(text):
        new_str = ""
        for char in text:
            if char != "":
                new_str += "_"
            else:
                new_str += " "
        return new_str

    def change_word(self, word):
        self.word = word

    def change_round(self, rnd):
        self.round = rnd
