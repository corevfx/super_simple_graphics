# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:02:05 2020

@author: MAYI
"""

import math, random 
from super_simple_graphics.canvas import *

w = 1000
h = 600
number_of_lines = 100
max_pen_width = 30

create_canvas(w,h)

for i in range(number_of_lines):
    set_pen_width(random.random()*max_pen_width)
    set_pen_color(random.random()*255,0,0,random.random()*255)
    draw_line(i*(w/number_of_lines), h, i*(w/number_of_lines), random.random()*h)
    
    
show_canvas()