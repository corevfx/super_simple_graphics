# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:06:25 2020

@author: Kevin Ma
"""

import math, random, sys
import super_simple_graphics.canvas as sg

w = 850
h = 480
number_of_text = 17
text_gap = 15
y_offset = -100

sg.create_canvas(w,h)
sg.fill_canvas_hsv(50,25,230)

    
sg.set_pen_width(2)
if sys.platform == "darwin":
    sg.set_font_n_style("Helvetica Neue",220,'Condensed Black')
elif sys.platform == "win32":
    sg.set_font_n_style("Arial Black",220,'Regular')

text = "TOKYO"
for i in range(0,number_of_text):
    sg.set_pen_color_hsv((i*(number_of_text-2)+180)%360,220,190)
    sg.draw_text(w/2,h-i*text_gap+y_offset,w,h,text)
  
sg.set_pen_color_hsv(0,0,0)
sg.draw_text(w/2,h-number_of_text*text_gap+y_offset,w,h,text)


sg.show_canvas()