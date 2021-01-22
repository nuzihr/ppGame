from .game import Game

class Player(object):

    def __init__(self, ip, name):
        self.game = None
        self.ip = ip
        self.name = name
        self.score = 0

    def add_score(self, x):
        self.score += x

    def get_score(self):
        return self.score

    def guess(self, string):
        pass

    def disconnect(self):
        pass
