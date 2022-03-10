
import pyray
import sys
import time

from sympy import as_finite_diff
sys.path.append('.')
from .gameScore import GameScore
from .screen.screenService import ScreenService
from .snake.snake1 import Snake1
from .snake.snake2 import Snake2
from .snake.tail import Tail
from .universe.pixel import Pixel
from .universe.universe import Universe

class Scheduler:

    def __init__(self):
        self.cols=60
        self.rows=40
        self.score1 = GameScore()
        self.score2 = GameScore()
        self.universe = Universe(self.cols,self.rows,self.score1,self.score2)
        self.pixel = Pixel()
        self.snake1 = Snake1()
        self.snake2 = Snake2()
        self._screenService = ScreenService(self.cols,self.rows,self.pixel)

    def playGame(self):
        done = False

        # Initialize graphics...
        self._screenService.open_window()

        # Start playing...
        timeStart = int(1000*time.time())
        while(self._screenService.is_window_open()):
            # Get keyboard inputs...
            x = pyray.get_key_pressed()
            self.snake1.get_direction(x)
            self.snake2.get_direction(x)
            if (self.getExit(x) == True):
                self._screenService.close_window()

            # Move snakes and check for collisions
            if (((int(1000*time.time())-timeStart)%100)==0): # Every 1/4 second move
                # Check to see if this is an adder time
                adder = False
                if (((int(1000*time.time())-timeStart)%3000)==0): # Every 3 seconds add
                    adder = True

                # Clear buffer before starting...
                self._screenService.clear_buffer()

                # Move snakes
                self.moveSnake(self.snake1,adder)
                self.moveSnake(self.snake2,adder)

                # Check for collisions

                # Output score

                # Flush buffer before moving on...
                self._screenService.flush_buffer()


    def getExit(self,x):
        if (x > 0):
            if (x == pyray.KEY_X): # left
                return True
        return False

    def moveSnake(self,snake,adder):
        # Draw the snake head
        x = snake.getX()+snake.getDX()*self.pixel.getPixelSize()
        y = snake.getY()+snake.getDY()*self.pixel.getPixelSize()
        if (x < 0):
            x = self.cols*self.pixel.getPixelSize()
        if (x > self.cols*self.pixel.getPixelSize()):
            x = self.pixel.getPixelSize()
        if (y < 0):
            y = self.rows*self.pixel.getPixelSize()
        if (y > self.rows*self.pixel.getPixelSize()):
            y = self.pixel.getPixelSize()
        # Get previous position
        x1 = snake.getX()+snake.getDX()*self.pixel.getPixelSize()
        y1 = snake.getY()+snake.getDY()*self.pixel.getPixelSize()
        # Get next position
        snake.setX(x)
        snake.setY(y)
        color = snake.getColor()
        icon = snake.getHead().getIcon()
        self._screenService.draw_icon(snake.getX(),snake.getY(),color,icon)

        # Set the snake tail
        tails = snake.getTails()
        if (adder == False):
            if (len(snake.getTails()) > 0):
                for i in range(len(tails)):
                    x2 = snake.getTails()[i].getX()
                    y2 = snake.getTails()[i].getY()
                    snake.getTails()[i].setX(x1)
                    snake.getTails()[i].setY(y1)
                    x1 = x2
                    y1 = y2
        else:
            for i in range(len(tails)):
                x2 = snake.getTails()[i].getX()
                y2 = snake.getTails()[i].getY()
                snake.getTails()[i].setX(x1)
                snake.getTails()[i].setY(y1)
                x1 = x2
                y1 = y2
            snake.getTails().append(Tail(x1,y1))
        
        # Output the tail
        if (len(snake.getTails()) > 0):
            icon = snake.getTails()[0].getIcon()
            for i in range(len(snake.getTails())):
                tail = snake.getTails()[i]
                x = int(tail.getX())
                y = int(tail.getY())
                self._screenService.draw_icon(x,y,color,icon)
        
        

