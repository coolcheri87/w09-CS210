


from .locn import Locn

class Tail(Locn):

    def __init__(self,x,y):
        super().__init__()
        self.icon = 'X'
        self.x = x
        self.y = y
    
    def getIcon(self):
        return self.icon
