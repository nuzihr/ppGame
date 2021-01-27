import pygame


class Leaderboard(object):

    def __init__(self, x, y, width=200, height=70):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.players = []
        self.name_font = pygame.font.SysFont("comicsans", 30, bold=True)
        self.score_font = pygame.font.SysFont("comicsans", 30)
        self.rank_font = pygame.font.SysFont("comicsans", 50, bold=True)
        self.BOARDER_THICKNESS = 5

    def draw(self, win):
        scores = [(player.get_name(), player.get_score()) for player in self.players]
        scores.sort(key=lambda x: x[1], reverse=True)

        for i, score in enumerate(scores):
            if i % 2 == 0:
                color = (255, 255, 255)
            else:
                color = (200, 200, 200)

            pygame.draw.rect(win, color, (self.x, self.y + i*self.height, self.width, self.height))

            rank = self.rank_font.render("#" + str(i+1), True, (0, 0, 0))
            win.blit(rank, (self.x + 10, self.y + i * self.height + (self.height - rank.get_height())/2))

            name = self.name_font.render(score[0], True, (0, 0, 0))
            win.blit(name, (self.x + 20 + (self.width - name.get_width())/2, self.y + 10 + i * self.height))

            score = self.score_font.render("Score: " + str(score[1]), True, (0, 0, 0))
            win.blit(score, (self.x + 20 + (self.width - name.get_width())/2, self.y + 40 + i * self.height))

        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height * len(self.players)), self.BOARDER_THICKNESS)

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)
