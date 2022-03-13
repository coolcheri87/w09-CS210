


import pyray
from .animal import Animal
from .getDirection import GetDirection


class Snake2(Animal):

    def __init__(self,x,y):
        super().__init__()
        self.name = 'Snake2'
        self.color = pyray.GREEN
        self.setX(x)
        self.setY(y)
        self._getDirection = GetDirection(pyray.KEY_J,pyray.KEY_I,pyray.KEY_K,pyray.KEY_L)

    def getName(self):
        return "I'm a slimy slithering " + self.name 

