# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:00:10 2020

@author: MAYI
"""

import math, random 
from super_simple_graphics.canvas import *

w=600
h=1000

number_of_points = 100
max_pen_width = 200

create_canvas(w,h)

for i in range(number_of_points):
    set_pen_width(random.random()*max_pen_width)
    set_pen_color(random.random()*255,0,0,random.random()*255)
    draw_point(i*(w/number_of_points), random.random()*h)
    
show_canvas()