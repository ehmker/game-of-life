from graphics import Window
from gameoflife import GameOfLife


def main():
    win = Window(600, 600)
    g = GameOfLife(20, 20, 40, 40, 10, win=win, seed=100)
    g.ran_start(0.1)
    win.start_main_loop(g, 5)
    win.wait_for_close()


main()
