


from .locn import Locn

class Head(Locn):

    def __init__(self):
        super().__init__()
        self.icon = 'O'
    
    def getIcon(self):
        return self.icon
