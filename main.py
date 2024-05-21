from graphics import Window
from gameoflife import GameOfLife


def main():
    win = Window(440, 440)
    g = GameOfLife(20, 20, 40, 40, 10, win=win, seed=199)
    g.ran_start(0.5)

    win.start_main_loop(g, 5)
    win.wait_for_close()


main()
