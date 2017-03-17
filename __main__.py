# coding=utf-8
"""
A main function for running an actual game.
"""

from __future__ import print_function

import os

from engine import Engine


def clear():
    """
    Method to clear the console.
    """
    os.system('cls')


def print_grid(grid_):
    """
    Method to nicely display the grid.
    :param grid: A grid to display.
     :type grid: list[list[int]]
    """
    n = 0
    for i in range(len(grid_)):
        n = len(grid_[i])
        print("      |" + "------|" * n)
        print("      |" + "      |" * n)
        line = "      |"
        for j in range(len(grid_[i])):
            line += str(grid_[i][j]).center(6) + "|"
        print(line)
        print("      |" + "      |" * n)
        print("      |" + "------|" * n)


if __name__ == "__main__":
    import msvcrt as conio

    grid = [[2, 2, 0, 2],
            [0, 0, 1, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0]]
    engine = Engine()
    engine._grid = grid
    clear()
    print_grid(engine._grid)

    key = conio.getch()

    while key != '\xe0':
        if key == '1':
            engine.left()
        elif key == '5':
            engine.up()
        elif key == '3':
            engine.right()
        elif key == '2':
            engine.down()
        clear()
        print_grid(engine._grid)
        key = conio.getch()
