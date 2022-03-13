


import pyray
from .animal import Animal
from .getDirection import GetDirection


class Snake1(Animal):

    def __init__(self,x,y):
        super().__init__()
        self.name = 'Snake1'
        self.color = pyray.YELLOW
        self.setX(x)
        self.setY(y)
        self._getDirection = GetDirection(pyray.KEY_A,pyray.KEY_W,pyray.KEY_S,pyray.KEY_D)

    def getName(self):
        return "I'm a slimy slithering " + self.name 

        