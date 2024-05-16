class Cell:
    def __init__(self, isAlive=False, win=None) -> None:
        self._win = win
        self.isAlive = False

    def draw(self, x, y, size):
        if self.isAlive:
            fill_color = "black"
        else:
            fill_color = "white"
        self._win._canvas.create_rectangle(x, y, x + size, y + size, fill=fill_color)

    def cell_enviroment_check(self, n):
        # updates isAlive status of cell depending on neighbor conditions
        # n = number of surrounding neighbors
        if self.isAlive:
            # Check for overpopulation
            if n > 3:
                self.isAlive = False
            # check underpopulation
            if n < 2:
                self.isAlive = False
        else:
            if n == 3:
                self.isAlive = True
