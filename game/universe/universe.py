

import sys
sys.path.append('.')
from .pixel import Pixel
from ..gameScore import GameScore


class Universe:

    def __init__(self,cols,rows,score1,score2):
        self.cols = cols
        self.rows = rows
        self.score1 = score1
        self.score2 = score2
        self.pixel = Pixel()

    def getCols(self):
        return self.cols

