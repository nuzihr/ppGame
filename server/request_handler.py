"""
MAIN THREAD
Handles all of the connections, creating new games and requests from the client(s).
"""

import socket
import threading
from .player import Player
from .game import Game
import json


class Server(object):
    def __init__(self):
        self.connection_queue = []
        self.game_id = 0

    def player_thread(self, conn, player):
        """
        handles in game communication between clients
        :param conn: connection object
        :param ip: str
        :param name: str
        :return: None
        """
        while True:
            try:
                data = conn.recv(1024)
                data = json.loads(data)

                keys = [keys for key in data.keys()]
                send_msg = {key: [] for key in keys}

                for key in keys:
                    if key == -1:
                    elif key == 0:
                    elif key == 1:
                    elif key == 2:
                    elif key == 3:
                    elif key == 4:
                    elif key == 5:
                    elif key == 6:
                    elif key == 7:
                    elif key == 8:
                    elif key == 9:

                conn.sendall(json.dumps(send_msg))
            except Exception() as e:
                print(f"[Exception] {player.name} disconnected: ", e)

    def handle_queue(self, player):
        """
        adds player to queue and creates new game if enough players
        :param player: Player
        :return: None
        """
        self.connection_queue.append(player)

        if len(self.connection_queue) >= 3:
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

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((server, port))
        except socket.error as e:
            str(e)

        s.listen()
        print("Waiting for a connectio, Server Started")

        while True:
            conn, addr = s.accept()
            print("[CONNECT] New Connection")
            self.authentication(conn, addr)


if __name__ == "__main__":
    s = Server()
    threading.Thread(target=s.connection_thread)
