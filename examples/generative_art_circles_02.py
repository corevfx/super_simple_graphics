# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:00:53 2020

@author: Kevin Ma
"""

import super_simple_graphics.canvas as sg
import random

w = 600
h = 1000

circles = []

for i in range(20):
    circles.append((random.uniform(0,w),random.uniform(0,h),random.uniform(30,180)))

# create windows
sg.create_canvas(w,h)

# draw thicker black background circles
for item in circles:
    sg.set_brush_color(255,255,255,0)
    sg.set_pen_color(0,0,0)
    sg.set_pen_width(9*2)
    sg.draw_circle(item[0],item[1],item[2])


# draw thicker white background circles    
for item in circles:
    sg.set_pen_color(255,255,255)
    sg.set_pen_width(3*2)
    sg.draw_circle(item[0],item[1],item[2])
    
sg.set_pen_style('NoPen')
sg.set_brush_color(0,200,150,220)
sg.draw_rect_with_rot_bl(0,350,w,150,0)

sg.set_pen_color(255,255,255)
sg.set_pen_style('SolidLine')
sg.set_font_size(44)
sg.draw_text(w/2,460,w,100,"Fantastic Circles")
sg.set_font_size(12)
sg.draw_text(w/2,420,w,100,"Generated by using Super Simple Graphics Python library")

# show windows
sg.show_canvas()