


class Animal:

    def __init__(self):
        self.name = 'Animal'
        self.len = 1
        self.x = 10
        self.y = 10

    # Getters
    def getName(self):
        return "I'm just an " + self.name

    def getLength(self):
        return self.len

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    # Setters
    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y