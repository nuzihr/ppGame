from board import Board
from round import Round
import random


class Game(object):

    def __init__(self, id, players):
        """
        init the game! once player threshold is met
        :param id: int
        :param players: Player[]
        """
        self.id = id
        self.players = players
        self.words_used = set()
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0
        self.round_count = 0
        self.start_new_round()

    def start_new_round(self):
        """
        Starts a new round with a new word
        :return: None
        """
        self.round = Round(self.get_word(), self.players[self.player_draw_ind], self)

        # if self.player_draw_ind >= len(self.players):
        #     self.end_round()
        #     self.end_game()

        self.round_count += 1
        self.player_draw_ind += 1

    def player_guess(self, player, guess):
        """
        Makes the player guess the word
        :param player: Player
        :param guess: str
        :return: bool
        """
        return self.round.guess(player, guess)

    def player_disconnected(self, player):
        """
        Call to clean up objects when player disconnects
        :param player: Player
        :raise Exception()
        """
        if player in self.players:
            player_idx = self.players.index(player)
            if player_idx <= self.player_draw_ind:
                self.player_draw_ind -= 1
            self.players.remove(player)
            self.round.player_left(player)
        else:
            raise Exception("Player not in game")

        if len(self.players) <= 2:
            self.end_game()

    def get_player_scores(self):
        """
        give a dict of player socres.
        :return: dict
        """
        return {player.get_name(): player.get_score() for player in self.players}

    def skip(self, player):
        """
        Increments the round skips, if skips are greater than threshold, starts new round.
        :return: None
        """
        if self.round:
            new_round = self.round.skip(player)
            if new_round:
                self.end_round()
                return True
            return False
        else:
            raise Exception("No round started yet.")
        pass

    def update_board(self, x, y, color):
        """
        calls update method on board.
        :param x: int
        :param y: int
        :param color: (int,int,int)
        :return: None
        """
        if not self.board:
            raise Exception("No board created")
        self.board.update(x, y, color)

    def end_round(self):
        """
        If the round ends call this
        :return: None
        """
        if len(self.players) > 1:
            self.start_new_round()
            self.board.clear()
        else:
            self.end_game()

    def end_game(self):
        """
        ends the game
        :return:
        """
        for player in self.players:
            player.game = None

    def get_word(self):
        """
        gives a word that has not yet been used
        :return: str
        """
        with open("./server/words.txt", "r") as f:
            words = []
            for line in f:
                word = line.strip()
                if word not in self.words_used:
                    words.append(word)

            r = random.randint(0, len(words)-1)
            w = words[r].strip()
            self.words_used.add(w)
            return w
