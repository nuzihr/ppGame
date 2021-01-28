import pygame


class Chat(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 250
        self.HEIGHT = 650
        self.content = ["Hiasdfghjkl;zxcvbnm,asdfghjklzxcvbnm," for _ in range(100)]
        self.typing = ""
        self.chat_font = pygame.font.SysFont("comicsans", 20)

    def update_chat(self, msg):
        self.content.append(msg)

    def draw(self, win):
        while len(self.content) > 20:
            self.content = self.content[:-1]
        for i, msg in enumerate(self.content):
            txt = self.chat_font.render(msg, 1, (0, 0, 0))
            win.blit(txt, (self.x+5, self.y + i * 30 + 10))

        pygame.draw.rect(win, (200, 200, 200),
                         (self.x, self.y + self.HEIGHT - 40, self.WIDTH, 40))
        pygame.draw.line(win, (0, 0, 0),
                         (self.x, self.y + self.HEIGHT - 40), (self.x + self.WIDTH, self.y + self.HEIGHT - 40), 5)
        type_chat = self.chat_font.render(self.typing, 1, (0, 0, 0))
        win.blit(type_chat, (self.x + 5, self.y + self.HEIGHT - 40 + type_chat.get_height()/2))

        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.WIDTH, self.HEIGHT), 5)

    def type(self, char, delete=False):
        if char == "BACKSPACE":
            if len(self.typing) > 0:
                self.typing = self.typing[:-1]
        elif char == "SPACE":
            self.typing += " "
        elif len(char) == 1:
            if len(self.typing) > 19:
                self.typing = self.typing[:19]
            self.typing += char
