from game import Game


class Player(object):

    def __init__(self, ip, name):
        """
        init the player object
        :param ip: str
        :param name: str
        """
        self.ip = ip
        self.name = name
        self.score = 0
        # self.game = None
        self.game = Game("1", [self, self])

    def get_ip(self):
        return self.ip

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def add_score(self, x):
        """
        add a players score
        :param x:
        :return:
        """
        self.score += x

    def set_game(self, game):
        """
        sets the players game association
        :param game: Game
        :return: None
        """
        self.game = game

    def disconnect(self):
        """
        call to disconnect player
        :return:
        """
        self.game.player_disconnected(self)

    def guess(self, word):
        """
        makes a player guess
        :param word: str
        :return: bool
        """
        return self.game.player_guess(self, word)
