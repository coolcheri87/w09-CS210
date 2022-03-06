


from .animal import Animal


class Snake(Animal):

    def __init__(self):
        super.__init__(self)
        self.name = 'Snake'

    def getName(self):
        return "I'm a slithering " + self.name