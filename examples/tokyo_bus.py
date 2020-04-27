# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:25:50 2020

@author: Kevin Ma
"""

import super_simple_graphics.canvas as sg
import math, random

w = 600
h = 1000

bg_color = (200,200,200)
title = '東京バス'
font_size = 30
char_dist = 100

box_dist = 45

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def fit_range(v, s1, s2, t1, t2):
    if v<=s1:
        return t1
    if v>=s2:
        return t2
    return (t2-t1)*(v-s1)/(s2-s1) + t1

def layer_lines():
    sg.set_pen_width(1)
    for i in range(10):
        offset_x = random.uniform(-200,200)
        offset_y = random.uniform(-200,200)
        sg.draw_line((h-w)/2+w+offset_x,0+offset_x,-(h-w)/2+offset_y,h+offset_y)
        
def random_circles():
    sg.set_brush_style("NoBrush")
    sg.set_pen_width(1)
    for i in range(20):
        x = random.uniform(0,w)
        y = random.uniform(0,h)
        sg.draw_circle(x,y, random.uniform(10,500))

def set_gradient():
    sg.set_brush_style_linear_gradient(w, 0, 0, h, r1=183, g1=58, b1=255, r2=28, g2=5, b2=121)
    sg.set_brush_gradient_color_at(0.4, 255, 73, 167)


sg.create_canvas(w,h)

# fill the background with gradent color
set_gradient()
sg.draw_rect(w/2,h/2,w,h)

# bg layer 2
sg.set_pen_color(255,255,255,50)
layer_lines()

random_circles()
    
# draw the graphics 
set_gradient()
sg.translate_origin(w/2,h/2)
#sg.set_brush_style("SolidPattern")
sg.set_brush_color(255,0,0)
sg.set_pen_color(0,0,0,0)
sg.rotate_origin(45)
for m in range(-20,21):
    for n in range(-20,21):
        x = m*box_dist
        y = n*box_dist
        d = distance(x,y,0,0)
        nsize = fit_range(d,0,500,50,0)
        sg.draw_rect(x,y,nsize,nsize)
sg.reset_origin()

# bg layer 2
sg.set_pen_color(255,255,255,100)
layer_lines()
        
# draw the title
sg.set_font_size(font_size)
for i in range(len(title)):
    y = h/2-((len(title)-1)/2-i)*char_dist
    x = w/2
    sg.set_pen_color(255,255,255,50)
    for j in range(9):
        offset_x = random.uniform(-10,10)
        offset_y = random.uniform(-5,5)
        sg.translate_origin(x+offset_x,y+offset_y)
        sg.rotate_origin(random.uniform(-20,20))
        sg.draw_text(0,0,char_dist, char_dist, title[i])
        sg.reset_origin()
    sg.set_pen_color(255,255,255)
    sg.draw_text(x,y,char_dist, char_dist, title[i]) 

sg.show_canvas()