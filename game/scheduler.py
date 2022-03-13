
import pyray
import random
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
        self.snake1 = Snake1(random.randint(0,self.cols)*self.pixel.getPixelSize(),random.randint(0,self.rows)*self.pixel.getPixelSize())
        self.snake2 = Snake2(random.randint(0,self.cols)*self.pixel.getPixelSize(),random.randint(0,self.rows)*self.pixel.getPixelSize())
        self._screenService = ScreenService(self.cols,self.rows,self.pixel)

    def playGame(self):
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
            if (((int(1000*time.time())-timeStart)%250)==0): # Every 1/4 second move
                # Check to see if this is an adder time
                adder = False
                if (((int(1000*time.time())-timeStart)%3000)==0): # Every 3 seconds add
                    adder = True

                # Clear buffer before starting...
                self._screenService.clear_buffer()

                # Move snakes
                self.moveSnake(self.snake1,adder)
                self.check4Collisions(self.snake1,self.snake2)
                self.moveSnake(self.snake2,adder)
                self.check4Collisions(self.snake2,self.snake1)

                # Check for collisions

                # Output score
                self.outputScore()

                # Flush buffer before moving on...
                self._screenService.flush_buffer()


    def outputScore(self):
        out1 = "%s%s%s %s,%s"%(self.snake1.name," - Score = ",self.score1.getScore(),self.snake1.getX(),self.snake1.getY())
        out2 = "%s%s%s %s,%s"%(self.snake2.name," - Score = ",self.score2.getScore(),self.snake2.getX(),self.snake2.getY())
        x1 = self.pixel.getPixelSize()
        x2 = (self.cols-len(out2))*self.pixel.getPixelSize()
        y = (self.rows+1)*self.pixel.getPixelSize()
        self._screenService.draw_icon(x1,y,pyray.WHITE,out1)
        self._screenService.draw_icon(x2,y,pyray.WHITE,out2)


    def check4Collisions(self,snake1,snake2):
        # Check for snake1
        safe = True
        x1 = snake1.getX()
        y1 = snake1.getY()
        x2 = snake2.getX()
        y2 = snake2.getY()
        # Check for head to head collision
        if ((x1 == x2) and (y1 == y2)):
            return False

        # Check for snake1 to own tail collision
        if (not safe):
            tail = self.snake1.getTails()
            for i in range(tail):
                if ((x1 == tail[i].getX()) and (y1 == tail[i].getY())):
                    safe = False
        # Check for snake1 to other snake tail collision
        if (not safe):
            tail = self.snake2.getTails()
            for i in range(tail):
                if ((x1 == tail[i].getX()) and (y1 == tail[i].getY())):
                    safe = False
        if (not safe):
            self.score2.incrementScore()

        return (safe) # Handle collisions...


    def getExit(self,x):
        if (x > 0):
            if (x == pyray.KEY_X): # left
                return True
        return False


    def moveSnake(self,snake,adder):
        # Draw the snake head at new location...
        # Current position
        x1 = snake.getX()
        y1 = snake.getY()
        # New position
        x = x1+snake.getDX()*self.pixel.getPixelSize()
        y = y1+snake.getDY()*self.pixel.getPixelSize()

        # Handle moving off the screen...
        if (x < 0):
            x = self.cols*self.pixel.getPixelSize()
        if (x > self.cols*self.pixel.getPixelSize()):
            x = self.pixel.getPixelSize()
        if (y < 0):
            y = self.rows*self.pixel.getPixelSize()
        if (y > self.rows*self.pixel.getPixelSize()):
            y = self.pixel.getPixelSize()

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
        
