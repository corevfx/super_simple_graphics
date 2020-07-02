# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:44:27 2020

@author: Kevin Ma
"""

import super_simple_graphics.canvas as sg
import random

w = 600
h = 1000
gap = 5

# create canvas
sg.create_canvas(w,h)

# set the image to the buffer first
sg.set_buffer_image("../images/aphrodite.jpg")

# sample the buffer image at the points with distance of pixels specified by gap variable
for i in range(int(w/gap)):
    for j in range(int(h/gap)):
        color = sg.get_color_from_buffer_image(i*gap,j*gap)
        sg.set_pen_width((1-color[0]/255.0)*10*random.uniform(0.8,1.2))
        sg.set_pen_color(color[0],color[1],color[2])
        sg.draw_point(i*gap+random.uniform(-1,1),j*gap+random.uniform(-1,1))
        
sg.show_canvas()