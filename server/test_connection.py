import socket
import json
import time

class Network:
    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.name = name

    def connect(self):
        try:
            self.client.connect(self.addr)
            self.client.send(self.name.encode())
            return self.client.recv(2048).decode()
        except Exception as e:
            self.disconnect(e)

    def send(self, data):
        try:
            self.client.send(json.dumps(data).encode())
            return self.client.recv(2048).decode()
        except socket.error as e:
            self.disconnect(e)

    def disconnect(self, msg):
        print("[EXCEPTION] Disconnected from server", msg)
        self.client.close()


try:
    n = Network("qazaq39os")
    print(n.connect())
    # print(n.send({"-1": ""}))
    # print(n.send({"0": "hello"}))
    # print(n.send({"1": ""}))
    # print(n.send({"2": ""}))
    # print(n.send({"3": ""}))
    # print(n.send({"4": ""}))
    # print(n.send({"5": ""}))
    # print(n.send({"6": ""}))
    # print(n.send({"7": ""}))
    # print(n.send({"8": (0, 0, (0, 0, 0))}))
    print(n.send({"9": ""}))
    time.sleep(5)
    print(n.send({"9": ""}))
except Exception as e:
    print(e)
