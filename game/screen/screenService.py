
import pyray as pr
import sys
sys.path.append('.')


class ScreenService:

    def __init__(self, width, height, fallers):
        self._width = width
        self._height = height+1
        self._cell_size = 30
        self._fallers = fallers

    def close_window(self):
        pr.close_window()

    def clear_buffer(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
    
    def draw_faller(self, faller, x):
        text = faller.getSymbol()
        y = faller.getHeight()
        pr.draw_text(text,x*self._cell_size,y*self._cell_size,self._cell_size,faller.getColor())

    def draw_fallers(self, fallers):
        for x in range(0,self._width):
            self.draw_faller(fallers[x],x)

    def draw_player(self, player):
        x = player.getX()*self._cell_size
        y = (self._height-1)*self._cell_size
        pr.draw_text(player.getSymbol(),x,y,self._cell_size,pr.YELLOW)
        y = self._height*self._cell_size
        text = 'Player: ' + player.getName() + " - Score: " + str(player.getScore())
        pr.draw_text(text,0,y,self._cell_size,pr.WHITE)


    def flush_buffer(self):
        pr.end_drawing()

    def get_cell_size(self):
        return self._cell_size

    def get_height(self):
        return self._height

    def is_window_open(self):
        return not pr.window_should_close()

    def open_window(self):
        pr.init_window(self._width*self._cell_size, (self._height+1)*self._cell_size, 'Greed 1.00.20220219')
        pr.set_target_fps(30)
