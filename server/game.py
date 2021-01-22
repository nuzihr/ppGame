from .player import Player
from .board import Board
from .round import Round

class Game(object):

    def __init__(self, id, players, thread):
        """
        init the game! once player threshold is met
        :param id: int
        :param players: Player[]
        :param thread:
        """
        self.id = id
        self.players = players
        self.words_used = []
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0
        self.connected_thread = thread
        self.start_new_round()


    def start_new_round(self):
        """
        Starts a new round with a new word
        :return: None
        """
        self.round = Round(self.get_word(), self.players[self.player_draw_ind], self.players, self)
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.end_round()
            self.end_game()



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
        pass

    def skip(self):
        """
        Increments the round skips, if skips are greater than threshold, starts new round.
        :return: None
        """
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.end_round()
            pass
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
        self.start_new_round()
        self.board.clear()

    def end_game(self):
        """
        ends the game
        :return:
        """
        pass

    def get_word(self):
        """
        gives a word that has not yer used
        :return: str
        """
        pass
