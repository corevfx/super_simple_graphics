# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:15:43 2020

@author: Kevin Ma
"""


import super_simple_graphics.canvas as sg

sg.create_canvas(600,1000)
sg.fill_canvas(255,200,200)

sg.draw_image(0,1000,0,0,800,1000,"../images/aphrodite.jpg")

sg.set_pen_width(1)
sg.set_pen_color(255,255,255)
for i in range(10):
    sg.rotate_origin(10)
    sg.draw_line(0,0,0,1500)
    
sg.reset_origin()
    
sg.set_pen_color(255,0,0,0)
sg.set_brush_color(255,0,0,100)
sg.draw_rect(250,600,500,600)

text = 'CREATIVECODE'

for i in range(len(text)):
    sg.set_pen_color(255,255,255)
    sg.set_font_n_style("Kozuka Gothic Pr6N B",30,"Black")
    sg.draw_text((i%4)*100+100,750-int(i/4)*150,500,200,text[i])

sg.show_canvas()