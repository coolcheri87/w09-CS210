
import pyray as pr
import sys
sys.path.append('.')
from ..universe.pixel import Pixel


class ScreenService:

    def __init__(self, width, height, pixel):
        self._width = width
        self._height = height+1
        self._pixel = pixel
        self._cell_size = self._pixel.getPixelSize()

    def clear_buffer(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
    
    def flush_buffer(self):
        pr.end_drawing()

    def get_cell_size(self):
        return self._cell_size

    def get_height(self):
        return self._height

    # This is how we start
    def open_window(self):
        pr.init_window(self._width*self._cell_size, (self._height+1)*self._cell_size, 'Greed 1.00.20220219')
        pr.set_target_fps(30)

    # This is how we see if it is still open
    def is_window_open(self):
        return not pr.window_should_close()

    # This is how we draw an icon onto the screen
    def draw_icon(self,x,y,color,icon):
        pr.draw_text(icon,x,y,self._cell_size,color)

    # This is how we end
    def close_window(self):
        pr.close_window()

