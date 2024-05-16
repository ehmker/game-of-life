from graphics import Window
from gameoflife import GameOfLife


def main():
    win = Window(600, 600)
    g = GameOfLife(20, 20, 55, 55, 10, win=win)
    g.ran_start(0.05)
    win.start_main_loop(g, 1)
    win.wait_for_close()


main()
