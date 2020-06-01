
from ezgraphics import *

from ezgraphics import GraphicsWindow
can = GraphicsWindow()

teller = 0
x_pos = 10

while teller < 9:
    can.DrawRectangle(x_pos, 100, 50,50)
    teller+=1
