# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:24:24 2020

@author: Kevin Ma
"""

import super_simple_graphics.canvas as sg
import random

w = 1000
h = 600

def draw_panda(x, y):
    # ears
    sg.set_pen_color(0,0,0)
    sg.set_pen_width(50)
    sg.draw_point(x-50,y-75)
    sg.draw_point(x+50,y-75)
    # face
    sg.set_pen_color(255,255,255)
    sg.set_pen_width(150)
    sg.draw_point(x,y)
    # eyes
    sg.set_pen_color(0,0,0,0)
    sg.set_brush_color(0,0,0)
    sg.draw_ellipse_with_rot(x-30,y+10,50,30,-60)
    sg.draw_ellipse_with_rot(x+30,y+10,50,30,60)
    sg.set_pen_color(255,255,255)
    sg.set_pen_width(10)
    sg.draw_point(x-25,y+5)
    sg.draw_point(x+25,y+5)
    
    # nose
    sg.set_pen_color(0,0,0,0)
    sg.set_brush_color(0,0,0)
    sg.draw_ellipse(x,y+20,20,15)
    
    # mouth
    sg.set_pen_color(0,0,0)
    sg.set_pen_width(2)
    sg.draw_line(x,y+20,x,y+40)
    sg.draw_elliptical_arc(x,y+30,20,10,180,180)


sg.create_canvas(w,h)
sg.fill_canvas(200,200,200)

for i in range(10):
    for j in range(3):
        draw_panda(i*200+100,j*200+100)

sg.show_canvas()