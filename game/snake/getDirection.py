

import pyray
import random


class GetDirection:

    # Initialize direction getter with assigned keystrokes
    def __init__(self,left,up,down,right):
        self._dx = 0
        self._dy = 0
        # Assigned key strokes
        self._left = left
        self._up = up
        self._down = down
        self._right = right
        # Randomly start in a direction
        r = random.randint(0,3)
        if (r == 0):
            self._dx = -1
        if (r == 1):
            self._dx = 1
        if (r == 2):
            self._dy = -1
        if (r == 3):
            self._dy = 1


    # Change direction
    def get_direction(self,x):
        if (x > 0):
            if (x == self._left): # left
                if (self._dx == 0):
                    self._dx = -1
                self._dy = 0
            if (x == self._right): # right
                if (self._dx == 0):
                    self._dx = 1
                self._dy = 0
            if (x == self._down): # down
                self._dx = 0
                if (self._dy == 0):
                    self._dy = 1
            if (x == self._up): # up
                self._dx = 0
                if (self._dy == 0):
                    self._dy = -1

    def getDX(self):
        return self._dx

    def getDY(self):
        return self._dy