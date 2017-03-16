# coding=utf-8
"""
Test the engine of the engine-of-2048-game game.
"""

from unittest import TestCase

from engine import Engine


class TestEngine(TestCase):
    """
    Test class for the game's engine.
    """

    def setUp(self):
        """
        Setting up a game engine to run on.
        """
        self._engine = Engine()

    def test_engine(self):
        """
        Some tests to see if the engine works as it should.
        """
        grid = list([i * 4 + j for j in range(4)] for i in range(4))
        self._engine._grid = grid
        self._engine._rotate(2)
        self._engine._rotate(2)
        self.assertEqual(self._engine.grid, grid)
