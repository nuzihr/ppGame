"""
MAIN THREAD
Handles all of the connections, creating new games and requests from the client(s).
"""

import socket
import threading
from player import Player
from game import Game
import json


class Server(object):
    MIN_PLAYERS = 3
    MAX_PLAYERS = 8

    def __init__(self):
        self.connection_queue = []
        self.game_id = 0

    def player_thread(self, conn, player):
        """
        handles in game communication between clients
        :param conn: connection object
        :param player:
        :return: None
        """
        while True:
            try:
                data = conn.recv(1024)
                data = json.loads(data)

                keys = [key for key in data.keys()]
                send_msg = {key: [] for key in keys}

                for key in keys:
                    if key == -1:  # get game, return a list of players
                        if player.game:
                            send_msg[-1] = player.game.players
                        else:
                            send_msg[-1] = []

                    if player.game:
                        if key == 0:  # guess
                            correct = player.game.player_guess(player, data[0][0])
                            send_msg[0] = correct
                        elif key == 1:  # skip
                            skip = player.game.skip()
                            send_msg[1] = skip
                        elif key == 2:  # get chat
                            content = player.game.round.chat.get_chat()
                            send_msg[2] = content
                        elif key == 3:  # get board
                            board = player.game.board.get_board()
                            send_msg[3] = board
                        elif key == 4:  # get score
                            scores = player.game.get_player_scores()
                            send_msg[4] = scores
                        elif key == 5:  # get round
                            round = player.game.round_count
                            send_msg[5] = round
                        elif key == 6:  # get word
                            word = player.game.get_word()
                            send_msg[6] = word
                        elif key == 7:  # get skips
                            skips = player.game.round.skips
                            send_msg[7] = skips
                        elif key == 8:  # update board
                            x, y, color = data[8][:3]
                            player.game.update_board(x, y, color)
                        elif key == 9:  # get round time
                            t = player.game.round.time
                            send_msg[9] = t
                        else:
                            raise Exception("Not a valid request")

                conn.sendall(json.dumps(send_msg))
            except Exception() as e:
                print(f"[Exception] {player.get_name()} disconnected: ", e)
                conn.close()

    def handle_queue(self, player):
        """
        adds player to queue and creates new game if enough players
        :param player: Player
        :return: None
        """
        self.connection_queue.append(player)

        if len(self.connection_queue) >= self.MIN_PLAYERS:
            game = Game(self.game_id, self.connection_queue[:])
            self.game_id += 1

            for p in self.connection_queue:
                p.set_game(game)
            self.connection_queue = []

    def authentication(self, conn, addr):
        """
        authentication here
        :param conn: connection object
        :param addr: str
        :return: None
        """
        try:
            data = conn.recv(16)
            name = str(data.decode())
            if not name:
                raise Exception("No name received")
            conn.sendall("1".encode())
            player = Player(addr, name)
            self.handle_queue(player)
            threading.Thread(target=self.player_thread, args=(conn, player))
        except Exception as e:
            print("[EXCEPTION]", e)
            conn.close()

    def connection_thread(self):
        server = ""
        port = 5555

        svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            svr.bind((server, port))
        except socket.error as e:
            str(e)

        svr.listen()
        print("Waiting for a connection, Server Started")

        while True:
            conn, addr = svr.accept()
            print("[CONNECT] New Connection")
            self.authentication(conn, addr)


if __name__ == "__main__":
    s = Server()
    threading.Thread(target=s.connection_thread)
