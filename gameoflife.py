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
        self._living_cells = []
        self._cells = self._create_cells()

    def _create_cells(self):
        cell_matrix = []
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                c = Cell(i, j, self._x1, self._y1, self._cell_size, win=self._win)
                c.draw()
                row.append(c)

            cell_matrix.append(row)
        return cell_matrix

    def _draw_cells_init(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].draw()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()

    def _check_neighbors(self):
        ######################################################################################################################
        # function will iterate over the list of currently alive cells                                                       #
        # each iteration, add neighboring cells to the checked_cells set and increment the cell's neighbors attribute        #
        # then iterate over the checked_cells set to update the isAlive attribute and reset neighbors to 0 for future cycles #
        ######################################################################################################################

        updated_living_cells = []
        checked_cells = set()
        # print(self._living_cells)
        for cell in self._living_cells:
            i, j = cell[0], cell[1]
            checked_cells.add(self._cells[i][j])
            if i - 1 >= 0 and j - 1 >= 0:
                checked_cells.add(self._cells[i - 1][j - 1])
                self._cells[i - 1][j - 1].neighbors += 1

            if j - 1 >= 0:
                checked_cells.add(self._cells[i][j - 1])
                self._cells[i][j - 1].neighbors += 1

            if i + 1 < self._num_cols and j - 1 >= 0:
                checked_cells.add(self._cells[i + 1][j - 1])
                self._cells[i + 1][j - 1].neighbors += 1

            if i - 1 >= 0:
                checked_cells.add(self._cells[i - 1][j])
                self._cells[i - 1][j].neighbors += 1

            if i + 1 < self._num_cols:
                checked_cells.add(self._cells[i + 1][j])
                self._cells[i + 1][j].neighbors += 1

            if i - 1 >= 0 and j + 1 < self._num_rows:
                checked_cells.add(self._cells[i - 1][j + 1])
                self._cells[i - 1][j + 1].neighbors += 1

            if j + 1 < self._num_rows:
                checked_cells.add(self._cells[i][j + 1])
                self._cells[i][j + 1].neighbors += 1

            if i + 1 < self._num_cols and j + 1 < self._num_rows:
                checked_cells.add(self._cells[i + 1][j + 1])
                self._cells[i + 1][j + 1].neighbors += 1

        for cell in checked_cells:
            if cell.isAlive:
                updated_living_cells.append(cell.get_mx_location())
            cell.enviroment_check()

        self._living_cells = updated_living_cells

    def ran_start(self, density: float):
        updated_living_cells = []
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                if random.random() < density:
                    self._cells[i][j].isAlive = True
                    updated_living_cells.append((i, j))

        self._living_cells = updated_living_cells
