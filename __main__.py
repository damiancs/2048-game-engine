# coding=utf-8
"""
A main function for running an actual game.
"""

from __future__ import print_function

import os
from Tkinter import Tk, Frame, Button

from engine import Engine


class Application(Frame, object):
    """
    asdas
    """
    COLORS = {"0": {"bg": "white", "fg": "black"},
              "2": {"bg": "#eee4da", "fg": "black"},
              "4": {"bg": "#ede0c8", "fg": "black"},
              "8": {"bg": "#f2b179", "fg": "white"},
              "16": {"bg": "#f59563", "fg": "white"},
              "32": {"bg": "#f67c5f", "fg": "white"},
              "64": {"bg": "#f65e3b", "fg": "white"},
              "128": {"bg": "#edcf72", "fg": "white"},
              "256": {"bg": "#edcc61", "fg": "white"},
              "512": {"bg": "#edc850", "fg": "white"},
              "1024": {"bg": "#edc53f", "fg": "white"},
              "2048": {"bg": "#edc22e", "fg": "white"},
              "4096": {"bg": "", "fg": ""},
              "8192": {"bg": "", "fg": ""},
              "16384": {"bg": "", "fg": ""},
              "32768": {"bg": "", "fg": ""},
              "65536": {"bg": "", "fg": ""},
              "131072": {"bg": "", "fg": ""}}

    def __init__(self, master=None):
        """

        :param master:
        """
        super(Application, self).__init__(master)
        self.grid()
        self._engine = Engine()
        self._buttons = list()
        self.create_buttons()
        master.bind("<Left>", self._left)
        master.bind("<Right>", self._right)
        master.bind("<Up>", self._up)
        master.bind("<Down>", self._down)

    def _left(self, event=None):
        self._show(self._engine.left())

    def _right(self, event=None):
        self._show(self._engine.right())

    def _up(self, event=None):
        self._show(self._engine.up())

    def _down(self, event=None):
        self._show(self._engine.down())

    def _show(self, result):
        for i in range(self._engine.size):
            for j in range(self._engine.size):
                self._buttons[i][j]["text"] = str(result[2][i][j]) if result[2][i][j] else ""
                self._buttons[i][j]["bg"] = Application.COLORS[str(result[2][i][j])]["bg"]
                self._buttons[i][j]["fg"] = Application.COLORS[str(result[2][i][j])]["fg"]

    def create_buttons(self):
        """

        :return:
        """
        for i in range(self._engine.size):
            self._buttons.append(list())
            for j in range(self._engine.size):
                self._buttons[i].append(Button(self, text=self._engine.grid[i][j] if self._engine.grid[i][j] else "",
                                               height=4, width=10,
                                               **Application.COLORS[str(self._engine.grid[i][j])]))
        for i in range(self._engine.size):
            for j in range(self._engine.size):
                self._buttons[i][j].grid(row=i, column=j)


if __name__ == "__main__":
    wnd = Tk()
    app = Application(wnd)
    app.mainloop()

    try:
        wnd.destroy()
    except:
        pass
