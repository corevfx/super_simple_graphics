# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:23:42 2020

@author: Kevin Ma
"""

import math, random
import super_simple_graphics.canvas as sg

data = {"Product A":0.44, "Product B":0.28, "Product C":0.23, "Product D":0.05}

sg.create_canvas(600,1000)
sg.fill_canvas_hsv(160,100,240)

dis_centre = 10

sg.set_font("Arial",20)
sg.draw_text(300,100,600,100,"2019 Desktop Product Share")
sg.set_font("Arial",10)
sg.draw_text(300,150,600,100,"- A Professional Survey")

current_angle = 0
for key, value in data.items():
    sg.set_pen_width(1)
    sg.set_pen_color(0,0,0)
    middle_angle = (current_angle + current_angle + 360*value)/2.0
    sg.set_brush_color(random.randrange(100,255),180,random.randrange(100,255))
    sg.draw_pie(300+dis_centre*math.cos(math.radians(middle_angle)),500+dis_centre*math.sin(math.radians(middle_angle)),200,current_angle, 360*value)
    sg.draw_text(   300+100*math.cos(math.radians(middle_angle)),
                     500+100*math.sin(math.radians(middle_angle)),
                     200, 50,
                     key+" "+format(value*100,'.0f')+"%")
    current_angle = current_angle + 360*value

sg.show_canvas()