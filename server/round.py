from _thread import *
from chat import Chat


class Round(object):

    def __init__(self, word, player_drawing, players, game):
        """
        init object
        :param game: Game
        :param word: str
        :param player_drawing: Player
        :param players: Player[]
        """
        self.game = game
        self.word = word
        self.player_drawing = player_drawing
        self.player_scores = {player: 0 for player in players}
        self.player_guessed = []
        self.skips = 0
        self.time = 60
        self.chat = Chat(self)
        start_new_thread(self.time_thread, ())

    def skip(self):
        """
        Returns true if round
        :return:
        """
        self.skips += 1
        if self.skips > len(self.player_guessed) - 1:
            return True
        return False

    def get_scores(self):
        """
        :return: returns all the player scores
        """
        return self.scores

    def get_score(self, player):
        """
        gets a specific players scores
        :param player:
        :return: int
        """
        if player in self.player_scores:
            return self.player_scores[player]
        else:
            raise Exception("Player not in score list")

    def time_thread(self):
        """
        Run in thread to keep track of time
        :return: None
        """
        self.time -= 1
        if self.time <= 0:
            self.end_round("Time is up")

    def guess(self, player, word):
        """
        :returns bool if player got guess correct answer
        :param player: Player
        :param word: str
        :return bool
        """
        correct = (word == self.word)
        if correct:
            self.player_guessed.append(player)

    def player_left(self, player):
        """
        removes player that left from scores and list
        :param player: Player
        :return: None
        """
        if player in self.player_scores:
            del self.player_scores[player]

        if player in self.player_guessed:
            self.player_guessed.remove(player)

        if player == self.player_drawing:
            self.end_round("Drawing player leaves")

    def end_round(self, msg):

        for player in self.players:
            player.update_score(self.player_scores[player])
        self.game.end_round()
