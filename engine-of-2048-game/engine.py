# coding=utf-8
"""
The engine-of-2048-game game engine.
"""

import random


class Engine(object):
    """
    This is the engine-of-2048-game game engine.
    It implements a configurable game engine and exposes 4 big methods:
     - left;
     - up;
     - right;
     - down.
    These methods will always return the game status at a time.
    """

    def __init__(self, size=4, goal=11, goal_pass=True):
        """

        :param size:
         :type size: int
        :param goal:
         :type goal: int
        :param goal_pass:
         :type goal_pass: bool
        """
        self._size = size
        self._goal = goal
        self._goal_pass = goal_pass

        self._grid = list([0 for j in range(self._size)] for i in range(self._size))
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
        return 2 if random.randint(1, 100) <= 10 else 1

    def _status(self):
        """
        Calculates and returns the game status after a move is done.
        :return: The status of the game.
         :rtype: tuple[bool, bool]
        """
        # TODO: Implement this method
        return True, False

    def _rotate(self, rotations=0):
        """
        Rotates the grid anticlockwise *rotations* times.
        :param rotations: The number of rotations to be done (-90 * rotations degrees).
         :type rotations: int
        :return: Nothing.
        """
        if rotations >= 4:
            rotations %= 4

        if rotations == 1:
            new_grid = list([0 for j in range(self._size)] for i in range(self._size))
            for i in range(self._size):
                for j in range(self._size):
                    new_grid[self._size - j - 1][i] = self._grid[i][j]
            for i in range(self._size):
                for j in range(self._size):
                    self._grid[i][j] = new_grid[i][j]
            del new_grid
        elif rotations == 2:
            for i in range(self._size / 2):
                self._grid[i], self._grid[self._size - i - 1] = self._grid[self._size - i - 1], self._grid[i]
                for j in range(self._size / 2):
                    self._grid[i][j], self._grid[i][self._size - j - 1] = self._grid[i][self._size - j - 1], \
                                                                          self._grid[i][j]
                    self._grid[self._size - i - 1][j], self._grid[self._size - i - 1][self._size - j - 1] = \
                        self._grid[self._size - i - 1][self._size - j - 1], self._grid[self._size - i - 1][j]
        elif rotations == 3:
            new_grid = list([0 for j in range(self._size)] for i in range(self._size))
            for i in range(self._size):
                for j in range(self._size):
                    new_grid[j][self._size - i - 1] = self._grid[i][j]
            for i in range(self._size):
                for j in range(self._size):
                    self._grid[i][j] = new_grid[i][j]
            del new_grid
        else:
            pass

    def _move(self):
        """
        Moves the tiles to the left as the default movement.
        The other movements are made after rotating the grid like:
         -  90 degrees anticlockwise for the *up* direction;
         - 180 degrees anticlockwise for the *right* direction;
         - 270 degrees anticlockwise for the *down* direction.
        :return: Nothing.
        """
        # TODO: Implement this method
        pass

    def left(self):
        """
        Moves the tiles to the left and returns the status of the game.
        :return: The status of the game (self._status).
         :rtype: tuple[bool, bool]
        """
        self._move()
        return self._status()

    def top(self):
        """
        Moves the tiles up and returns the status of the game.
        :return: The status of the game (self._status).
         :rtype: tuple[bool, bool]
        """
        self._rotate(1)
        self._move()
        self._rotate(3)
        return self._status()

    def right(self):
        """
        Moves the tiles to the right and returns the status of the game.
        :return: The status of the game (self._status).
         :rtype: tuple[bool, bool]
        """
        self._rotate(2)
        self._move()
        self._rotate(2)
        return self._status()

    def down(self):
        """
        Moves the tiles down and returns the status of the game.
        :return: The status of the game (self._status).
         :rtype: tuple[bool, bool]
        """
        self._rotate(3)
        self._move()
        self._rotate(1)
        return self._status()


if __name__ == "__main__":
    grid = list([i * 4 + j for j in range(4)] for i in range(4))
    engine = Engine()
    #engine._grid = grid
    for line in engine._grid:
        print line
    print '-' * 32
    engine.down()
    for line in engine._grid:
        print line
