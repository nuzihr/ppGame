class Board(object):
    ROWS = COLS = 720

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.board = self.create_board()

    def create_board(self):
        return [[(255, 255, 255) for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def draw(self, win):
        pass

    def click(self, x, y):
        pass

    def update(self, x, y, color):
        pass

    def clear(self):
        self.board = self.create_board()