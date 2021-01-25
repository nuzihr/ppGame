from _thread import *
import time as t
from chat import Chat


class Round(object):

    def __init__(self, word, player_drawing, game):
        """
        init object
        :param game: Game
        :param word: str
        :param player_drawing: Player
        """
        self.game = game
        self.word = word
        self.player_drawing = player_drawing
        self.player_scores = {player.get_name(): 0 for player in self.game.players}
        self.player_guessed = []
        self.player_skipped = []
        self.time = 60
        self.chat = Chat(self)
        start_new_thread(self.time_thread, ())

    def skip(self, player):
        """
        Returns true if all player skip
        :return: bool
        """
        if player not in self.player_skipped:
            self.chat.update_chat("{} votes to skip ({})".format(player.get_name(), len(self.player_skipped)))
            self.player_skipped.append(player)

        if len(self.player_skipped) == len(self.game.players) - 1:
            self.chat.update_chat("Round has been skipped.")
            return True
        return False

    def get_skips(self):
        return len(self.player_skipped)

    def get_scores(self):
        """
        :return: returns all the player scores
        """
        return self.player_scores

    def get_score(self, player):
        """
        gets a specific players scores
        :param player:
        :return: int
        """
        name = player.get_name()
        if name in self.player_scores:
            return self.player_scores[name]
        else:
            raise Exception("Player not in score list")

    def time_thread(self):
        """
        Run in thread to keep track of time
        :return: None
        """
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.end_round("Time is up")

    def guess(self, player, word):
        """
        :returns bool if player got guess correct answer
        :param player: Player
        :param word: str
        :return bool
        """
        if word == self.word:
            self.player_guessed.append(player)
            return True

        self.chat.update_chat("{} guessed {}".format(player.get_name(), word))
        return False

    def player_left(self, player):
        """
        removes player that left from scores and list
        :param player: Player
        :return: None
        """
        name = player.get_name()
        if name in self.player_scores:
            del self.player_scores[name]

        if player in self.player_guessed:
            self.player_guessed.remove(player)

        if player in self.player_skipped:
            self.player_skipped.remove(player)

        if player == self.player_drawing:
            self.end_round("Drawing player leaves")

        print("{} disconnected.".format(player.get_name()))

    def end_round(self, msg):
        for player in self.game.players:
            name = player.get_name()
            if name in self.player_scores:
                player.add_score(self.player_scores[name])
        self.game.end_round()
