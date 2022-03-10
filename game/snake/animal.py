

import pyray
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
        self.dx = 0
        self.dy = 0

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
        return self.dx

    def getDY(self):
        return self.dy

    def getX(self):
        return self.x

    def getY(self):
        return self.y


    # Setters
    def setLength(self,len):
        self.len = len
        
    # Movement and Location
    def setDX(self,dx):
        self.dx = dx

    def setDY(self,dy):
        self.dy = dy

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    # Set for fgh
    def get_direction(self,x):

        if (x > 0):
            if (x == pyray.KEY_F): # left
                self.dx = -1
                self.dy = 0
            if (x == pyray.KEY_H): # right
                self.dx = 1
                self.dy = 0
            if (x == pyray.KEY_G): # down
                self.dx = 0
                self.dy = 1
            if (x == pyray.KEY_T): # up
                self.dx = 0
                self.dy = -1
