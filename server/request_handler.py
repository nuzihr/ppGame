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
                try:
                    data = conn.recv(1024)
                    data = json.loads(data.decode())
                except Exception as e:
                    break

                print("[LOG] receive {}".format(data))
                if not player.game:
                    conn.send("-1".encode())

                send_msg = {}
                keys = [key for key in data.keys()]
                for key in keys:
                    if key == "-1":  # get game, return a list of players
                        send = {player.get_name(): player.get_score() for player in player.game.players}
                        send_msg[key] = send
                    elif key == "0":  # guess
                        correct = player.game.player_guess(player, data[key])
                        send_msg[key] = correct
                    elif key == "1":  # skip
                        skip = player.game.skip(player)
                        send_msg[key] = skip
                    elif key == "2":  # get chat
                        content = player.game.round.chat.get_chat()
                        send_msg[key] = content
                    elif key == "3":  # get board
                        board = player.game.board.get_board()
                        send_msg[key] = board
                    elif key == "4":  # get score
                        scores = player.game.get_player_scores()
                        send_msg[key] = scores
                    elif key == "5":  # get round
                        round = player.game.round_count
                        send_msg[key] = round
                    elif key == "6":  # get word
                        word = player.game.get_word()
                        send_msg[key] = word
                    elif key == "7":  # get skips
                        skips = player.game.round.get_skips()
                        send_msg[key] = skips
                    elif key == "8":  # update board
                        x, y, color = data[key][:3]
                        player.game.update_board(x, y, color)
                    elif key == "9":  # get round time
                        t = player.game.round.time
                        send_msg[key] = t
                    else:
                        conn.send("-1".encode())
                        raise Exception("Not a valid request")

                conn.send(json.dumps(send_msg).encode())
            except Exception as e:
                print("[Exception] {} {}".format(player.get_name(), e))
                break

        if player.game:
            player.game.player_disconnected(player)

        if player in self.connection_queue:
            self.connection_queue.remove(player)

        print("[DISCONNECT] {} disconnected".format(player.get_name()))
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
            name = data.decode()
            if not name:
                raise Exception("No name received")
            conn.send("1".encode())
            player = Player(addr, name)
            self.handle_queue(player)
            player_thread = threading.Thread(target=self.player_thread, args=(conn, player))
            player_thread.start()
        except Exception as e:
            print("[EXCEPTION]", e)
            conn.close()

    def connection_thread(self):
        server = "localhost"
        port = 5555

        svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            svr.bind((server, port))
        except socket.error as e:
            str(e)

        svr.listen(1)
        print("Waiting for a connection, Server Started")

        while True:
            conn, addr = svr.accept()
            print("[CONNECT] New Connection")
            self.authentication(conn, addr)


if __name__ == "__main__":
    s = Server()
    thread = threading.Thread(target=s.connection_thread)
    thread.start()
