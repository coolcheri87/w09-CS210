


from .score import Score
from universe.universe import Universe

class Scheduler:

    def __init__(self):
        self.cols=60
        self.rows=40
        self.score1 = Score()
        self.score2 = Score()
        self.universe = Universe(self.cols,self.rows,self.score1,self.score2)

    def playGame(self):
        done = False

        # Initialize graphics...

        # Start playing...
        while(not done):
            # Get keyboard inputs...
            # Move snakes
            # Check for collisions
            done = True


