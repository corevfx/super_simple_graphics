# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:07:03 2020

@author: Kevin Ma
"""

import super_simple_graphics.canvas as sg
import random

w = 600
h = 1000

def circle_stack(x, y, max_radius, num_of_circles, right_center):
    sg.set_brush_color(random.randrange(100,255),200,200)
    sg.set_pen_color(0,0,0)
    pen_width = 2
    sg.set_pen_width(pen_width)
    #draw the bg circle
    if right_center:
        sg.draw_circle(x-max_radius-pen_width,y,max_radius)
    else:
        sg.draw_circle(x+max_radius+pen_width,y,max_radius)
    
    # draw all the on-top circles with no filling color
    sg.set_brush_color(0,0,0,0)
    for i in range(num_of_circles):
        radius = max_radius*random.uniform(0,1)
        if right_center:
            sg.draw_circle(x-radius-pen_width,y,radius)
        else:
            sg.draw_circle(x+radius+pen_width,y,radius)

sg.create_canvas(w,h)

for i in range(w):
    right_center = True
    if random.uniform(-1, 1) > 0:
        right_center = False 
    circle_stack(random.uniform(0,w),random.uniform(0,h),random.uniform(30,80),random.randrange(3,10), right_center)

sg.show_canvas()