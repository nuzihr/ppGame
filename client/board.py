import pygame


class Board(object):
    ROWS = COLS = 65
    SIZE = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = self.create_board()

    def create_board(self):
        return [[(255, 255, 0) for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def draw(self, win):
        for y, _ in enumerate(self.board):
            for x, color in enumerate(_):
                pygame.draw.rect(win, color, (self.x + x * self.SIZE, self.y + y * self.SIZE, self.SIZE, self.SIZE), 0)

        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.ROWS * self.SIZE, self.COLS * self.SIZE), 5)

    def click(self, x, y):
        """
        returns None if not in board, otherwise place clicked on in terms of row and col
        :param x: float
        :param y: fload
        :return: (int, int) or None
        """
        row = int((x - self.x)/self.SIZE)
        col = int((y - self.y)/self.SIZE)

        if 0 <= row < self.ROWS and 0 <= col < self.COLS:
            return row, col
        return None

    def update(self, x, y, color):
        self.board[y][x] = color

    def clear(self):
        self.board = self.create_board()
