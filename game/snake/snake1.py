


import pyray
from .animal import Animal


class Snake1(Animal):

    def __init__(self):
        super().__init__()
        self.name = 'Snake'
        self.color = pyray.YELLOW
        self.dx = -1

    def getName(self):
        return "I'm a slithering " + self.nameI 

    # Set for asd
    def get_direction(self,x):

        if (x > 0):
            if (x == pyray.KEY_A): # left
                self.dx = -1
                self.dy = 0
            if (x == pyray.KEY_D): # right
                self.dx = 1
                self.dy = 0
            if (x == pyray.KEY_S): # down
                self.dx = 0
                self.dy = 1
            if (x == pyray.KEY_W): # up
                self.dx = 0
                self.dy = -1