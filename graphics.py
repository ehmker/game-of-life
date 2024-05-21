from tkinter import Tk, Canvas, Button


class Window:
    def __init__(self, w, h, game=None) -> None:
        self._root = Tk()
        self._root.title("Conway's Game of Life")

        self._canvas = Canvas(width=w, height=h)
        self._canvas.grid(row=0, column=0, columnspan=3)
        # self._canvas.pack()

        self._running = False

        self._root.protocol("WM_DELETE_WINDOW", self.close)

        self._btn_pause = Button(self._root, text="Pause", command=self.button_pause)
        self._btn_pause.grid(row=1, column=2)

        self._btn_start = Button(self._root, text="Start", command=self.button_start)
        self._btn_start.grid(row=1, column=0)

        self._btn_step = Button(self._root, text="Step", command=self.button_step)
        self._btn_step.grid(row=1, column=1)

        self._game_of_life = game

    def redraw(self):
        print("Redrawing grid")
        print("==========================================")
        self._canvas.delete("all")
        for row in self._game_of_life._cells:
            for cell in row:
                cell.draw()
        self._canvas.update()
        print("==========================================")
        self._root.update()
        self._root.update_idletasks()

    def wait_for_close(self):
        self._root.mainloop()

    def start_main_loop(self, game_of_life, update_interval):
        def loop():
            if self._running:
                game_of_life._check_neighbors()
                self._root.after(update_interval, loop)

        if self._game_of_life is None:
            self._game_of_life = game_of_life
        loop()

    def close(self):
        self._root.quit()

    def button_pause(self):
        self._running = False
        print("Pausing")

    def button_start(self):
        self._running = True
        print("Starting")
        self.start_main_loop(self._game_of_life, 5)

    def button_step(self):
        print("Steping")
        self._game_of_life._check_neighbors()
        self.redraw()
