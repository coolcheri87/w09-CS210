

import pyray
from .getDirection import GetDirection
from .head import Head
from .tail import Tail

class Animal:

    def __init__(self):
        self.name = 'Animal'
        self.head = Head()
        self.tails = []
        self.color = pyray.RED
        self.len = 1
        self.x = 10
        self.y = 10
        self._getDirection = GetDirection(pyray.KEY_F,pyray.KEY_T,pyray.KEY_G,pyray.KEY_H)

    # Getters
    def getColor(self):
        return self.color

    def getName(self):
        return "I'm just an " + self.name

    def getLength(self):
        return self.len

    def getHead(self):
        return self.head

    def getTails(self):
        return self.tails

    # Movement and location
    def getDX(self):
        return self._getDirection.getDX()

    def getDY(self):
        return self._getDirection.getDY()

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    # Setters
    def setLength(self,len):
        self.len = len
        
    # Location
    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    # Set for fgh
    def get_direction(self,x):
        self._getDirection.get_direction(x)
