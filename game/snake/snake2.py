


import pyray
from .animal import Animal


class Snake2(Animal):

    def __init__(self):
        super().__init__()
        self.name = 'Snake'
        self.color = pyray.GREEN
        self.dy = 1

    def getName(self):
        return "I'm a slithering " + self.nameI 

    # Set for jkl
    def get_direction(self,x):

        if (x > 0):
            if (x == pyray.KEY_J): # left
                self.dx = -1
                self.dy = 0
            if (x == pyray.KEY_L): # right
                self.dx = 1
                self.dy = 0
            if (x == pyray.KEY_K): # down
                self.dx = 0
                self.dy = 1
            if (x == pyray.KEY_I): # up
                self.dx = 0
                self.dy = -1