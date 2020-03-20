# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:05:08 2020

@author: MAYI
"""

from super_simple_graphics.canvas import *

create_canvas(600,200)

fill_canvas(255,200,200)
set_font_size(80)
draw_text(300,100,600,200,"Hello World")

show_canvas()