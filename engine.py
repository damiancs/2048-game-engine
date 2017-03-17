# coding=utf-8
"""
The engine-of-2048-game game engine.
"""

import random


class Engine(object):
    """
    This is the engine-of-2048-game game engine. The default values are:
     - size : 4 * 4;
     - goal to achieve : 2048;
     - can play after goal achieved? : True.

    It implements a configurable game engine and exposes 4 big methods:
     - left;
     - up;
     - right;
     - down.
    These methods will always return the game status at a time.
    """

    def __init__(self, size=4, goal=2048, goal_pass=True):
        """
        Construction the engine and spawning two new items in the grid.
        :param size: The size of the grid (default: 4 * 4).
         :type size: int
        :param goal: The goal that needs achieved (default: 2048).
         :type goal: int
        :param goal_pass: This shows if the user can play after the goal is achieved (default: True).
         :type goal_pass: bool
        """
        self._size = size
        self._goal = goal
        self._goal_pass = goal_pass

        self._grid = [[0 for j in range(self._size)] for i in range(self._size)]
        self._spawn(2)

    def _spawn(self, items=1):
        """
        Spawns *items* numbers on the grid.
        :param items: The number of items to spawn on the grid.
         :type items: int
        """
        for i in range(items):
            i, j = self._choose_position()
            self._grid[i][j] = self._choose_item()

    def _choose_position(self):
        """
        Chooses an empty position for the new spawned item.
        :return: The free position on which to spawn the new item.
         :rtype: tuple[int, int]
        """
        res = random.randint(0, self._size ** 2 - 1)
        i = res / 4
        j = res % 4
        while self._grid[i][j] != 0:
            res = random.randint(0, self._size ** 2 - 1)
            i = res / 4
            j = res % 4
        return i, j

    @staticmethod
    def _choose_item():
        """
        Chooses an item to spawn.
        :return: The new item to spawn.
         :rtype: int
        """
        return 4 if random.randint(1, 100) <= 10 else 2

    def _status(self):
        """
        Calculates and returns the game status after a move is done.
        :return: The status of the game represented by two boolean values meaning (Goal achieved?, Has move?).
         :rtype: tuple[bool, bool]
        """
        # TODO: Implement this method

        return True, False

    @staticmethod
    def _rotate(grid_, rotations=0):
        """
        Rotates a grid anticlockwise *rotations* times.
        :param rotations: The number of rotations to be done (-90 * rotations degrees).
         :type rotations: int
        :param grid_: The grid to rotate.
         :type grid_: list[list[int]]
        :return: The rotated list
         :rtype: list[list[int]]
        """
        size = len(grid_)
        new_grid = [[0 for j in range(size)] for i in range(size)]
        if rotations >= 4:
            rotations %= 4

        if rotations == 1:
            for i in range(size):
                for j in range(size):
                    new_grid[size - j - 1][i] = grid_[i][j]
        elif rotations == 2:
            new_grid = Engine._copy(grid_)
            for i in range(size / 2):
                new_grid[i], new_grid[size - i - 1] = list(reversed(new_grid[size - i - 1])), \
                                                      list(reversed(new_grid[i]))
            if size % 2:
                new_grid[size / 2].reverse()
        elif rotations == 3:
            for i in range(size):
                for j in range(size):
                    new_grid[j][size - i - 1] = grid_[i][j]
        else:
            return grid_

        return new_grid

    @staticmethod
    def _retract(grid_):
        """
        Eliminate the zeros from a grid.
        :param grid_: The grid to be updated.
         :type grid_: list[list[int]]
        :return: The new retracted grid.
         :rtype: list[list[int]]
        """
        new_grid = list()
        for i in range(len(grid_)):
            new_grid.append(list())
            for j in range(len(grid_[i])):
                if grid_[i][j]:
                    new_grid[i].append(grid_[i][j])
        return new_grid

    @staticmethod
    def _combine(grid_):
        """
        Combines the values of a grid and returns the new calculated grid.
        Note that the direction is from right to left. For other directions the _rotate method is used.
        :param grid_: The grid of which values need to be combined.
         :type grid_: list[list[int]]
        :return: The new grid with combined values.
         :rtype: list[list[int]]
        """
        new_grid = list()
        for i in range(len(grid_)):
            new_grid.append(list())
            swapped = False
            if len(grid_[i]) == 1:
                new_grid[i].append(grid_[i][0])
            elif len(grid_[i]) > 1:
                for j in range(len(grid_[i])):
                    if swapped:
                        swapped = False
                        continue
                    if j == len(grid_[i]) - 1:
                        new_grid[i].append(grid_[i][j])
                        continue
                    if grid_[i][j] == grid_[i][j + 1]:
                        new_grid[i].append(2 * grid_[i][j])
                        swapped = True
                    else:
                        new_grid[i].append(grid_[i][j])
                        swapped = False
        return new_grid

    @staticmethod
    def _expand(grid_):
        """
        Expands the size of each ot the grid's line to be the same size as the game grid.
        :param grid_: The grid to be updated.
         :type grid_: list[list[int]]
        :return: The expanded grid.
         :rtype: list[list[int]]
        """
        new_grid = Engine._copy(grid_)
        size = len(new_grid)
        for i in range(len(new_grid)):
            new_grid[i].extend([0] * (size - len(new_grid[i])))
        return new_grid

    @staticmethod
    def _same(old_grid, new_grid):
        """
        Check if two grids have the same pattern.
        :param old_grid: The old grid to check.
         :type old_grid: list[list[int]]
        :param new_grid: The new grid to check against.
         :type new_grid: list[list[int]]
        :return: A boolean value showing if the two grids are the same.
         :rtype: bool
        """
        if len(old_grid) != len(new_grid):
            return False
        for i in range(len(old_grid)):
            if len(old_grid[i]) != len(new_grid[i]):
                return False
            for j in range(len(old_grid)):
                if old_grid[i][j] != new_grid[i][j]:
                    return False
        return True

    @staticmethod
    def _move(grid_):
        """
        Moves the tiles to the left as the default movement in a grid.
        The other movements are made after rotating the grid like:
         -  90 degrees anticlockwise for the *up* direction;
         - 180 degrees anticlockwise for the *right* direction;
         - 270 degrees anticlockwise for the *down* direction.
        :return: The new grid with tiles moved.
         :rtype: list[list[int]]
        """
        new_grid = Engine._copy(grid_)
        new_grid = Engine._retract(new_grid)
        new_grid = Engine._combine(new_grid)
        new_grid = Engine._expand(new_grid)
        return new_grid

    @staticmethod
    def _copy(grid_):
        """
        This returns a copy of the grid sent as parameter.
        :param grid_: The grid to copy.
         :type grid_: list[list[int]]
        :return: A copy of the grid.
         :rtype: list[list[int]]
        """
        new_grid = list()
        for i in range(len(grid_)):
            new_grid.append(list())
            for j in range(len(grid_[i])):
                new_grid[i].append(grid_[i][j])
        return new_grid

    def left(self):
        """
        Moves the tiles to the left and returns the status of the game.
        :return: The status of the game (self._status).
         :rtype: tuple[bool, bool]
        """
        old_grid = self._copy(self._grid)
        self._grid = Engine._move(self._grid)
        if not Engine._same(old_grid, self._grid):
            self._spawn()
        return self._status()

    def up(self):
        """
        Moves the tiles up and returns the status of the game.
        :return: The status of the game (self._status).
         :rtype: tuple[bool, bool]
        """
        old_grid = self._copy(self._grid)
        self._grid = Engine._rotate(self._grid, 1)
        self._grid = Engine._move(self._grid)
        self._grid = Engine._rotate(self._grid, 3)
        if not Engine._same(old_grid, self._grid):
            self._spawn()
        return self._status()

    def right(self):
        """
        Moves the tiles to the right and returns the status of the game.
        :return: The status of the game (self._status).
         :rtype: tuple[bool, bool]
        """
        old_grid = self._copy(self._grid)
        self._grid = Engine._rotate(self._grid, 2)
        self._grid = Engine._move(self._grid)
        self._grid = Engine._rotate(self._grid, 2)
        if not Engine._same(old_grid, self._grid):
            self._spawn()
        return self._status()

    def down(self):
        """
        Moves the tiles down and returns the status of the game.
        :return: The status of the game (self._status).
         :rtype: tuple[bool, bool]
        """
        old_grid = Engine._copy(self._grid)
        self._grid = Engine._rotate(self._grid, 3)
        self._grid = Engine._move(self._grid)
        self._grid = Engine._rotate(self._grid, 1)
        if not Engine._same(old_grid, self._grid):
            self._spawn()
        return self._status()
