import random
from cell import Cell


class GameOfLife:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size, win=None, seed=None
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._win = win

        if seed:
            random.seed(seed)

        self._cells = self._create_cells()
        self._draw_cells()

    def _create_cells(self):
        cell_matrix = []
        for _ in range(self._num_rows):
            row = []
            for _ in range(self._num_cols):
                row.append(Cell(win=self._win))
            cell_matrix.append(row)
        return cell_matrix

    def _draw_cells(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].draw(
                    self._x1 + i * self._cell_size,
                    self._y1 + j * self._cell_size,
                    self._cell_size,
                )

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()

    def _check_neighbors(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                neighbor_count = 0
                if (i - 1 >= 0 and j - 1 >= 0) and self._cells[i - 1][j - 1].isAlive:
                    neighbor_count += 1

                if (j - 1 >= 0) and self._cells[i][j - 1].isAlive:
                    neighbor_count += 1

                if (i + 1 < self._num_cols and j - 1 >= 0) and self._cells[i + 1][
                    j - 1
                ].isAlive:
                    neighbor_count += 1

                if (i - 1 >= 0) and self._cells[i - 1][j].isAlive:
                    neighbor_count += 1

                if (i + 1 < self._num_cols) and self._cells[i + 1][j].isAlive:
                    neighbor_count += 1

                if (i - 1 >= 0 and j + 1 < self._num_rows) and self._cells[i - 1][
                    j + 1
                ].isAlive:
                    neighbor_count += 1

                if (j + 1 < self._num_rows) and self._cells[i][j + 1].isAlive:
                    neighbor_count += 1

                if (i + 1 < self._num_cols and j + 1 < self._num_rows) and self._cells[
                    i + 1
                ][j + 1].isAlive:
                    neighbor_count += 1

                self._cells[i][j].cell_enviroment_check(neighbor_count)

    def update_and_draw(self):
        self._check_neighbors()
        self._draw_cells()
        self._animate()

    def ran_start(self, density: float):
        for row in self._cells:
            for cell in row:
                if random.random() < density:
                    cell.isAlive = True
