# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:11:57 2020

@author: MAYI
"""

from super_simple_graphics.canvas import *

create_canvas(400,300)

set_pen_color(255,0,0)
set_pen_width(3)
set_brush_color(0,0,255)
draw_circle(150,100,80)

set_pen_color(0,255,255)
set_pen_width(8)
set_brush_color(255,255,0)
draw_rect(250,170,180,100)

show_canvas()