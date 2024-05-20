class Cell:
    def __init__(self, i, j, x_offset, y_offset, size, isAlive=False, win=None) -> None:
        self._win = win
        self.isAlive = False
        self.neighbors = 0
        self._x = x_offset + i * size  # (x, y) = coordinates of cell on canvas
        self._y = y_offset + j * size
        self._i = i  # (i, j) = coordinates of cell in matrix
        self._j = j
        self._size = size

    def draw(self):
        if self.isAlive:
            fill_color = "black"
        else:
            fill_color = "white"
        self._win._canvas.create_rectangle(
            self._x,
            self._y,
            self._x + self._size,
            self._y + self._size,
            fill=fill_color,
        )

    def enviroment_check(self):
        # updates isAlive status of cell depending on neighbor conditions
        # resets neighbor count for future cycles
        if self.isAlive:
            if self.neighbors > 3:
                self.isAlive = False
            if self.neighbors < 2:
                self.isAlive = False
        else:
            if self.neighbors == 3:
                self.isAlive = True

        self.neighbors = 0

    def get_mx_location(self):
        return (self._i, self._j)
