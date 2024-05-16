from tkinter import Tk, Canvas


class Window:
    def __init__(self, w, h) -> None:
        self._root = Tk()
        self._root.title("Conway's Game of Life")

        self._canvas = Canvas(width=w, height=h)
        self._canvas.pack()

        self._running = False

        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update()
        self._root.update_idletasks()

    def wait_for_close(self):
        self._root.mainloop()

    def start_main_loop(self, game_of_life, update_interval):
        def loop():

            game_of_life._check_neighbors()
            game_of_life._draw_cells()
            self._root.after(update_interval, loop)

        loop()

    def close(self):
        self._root.quit()
