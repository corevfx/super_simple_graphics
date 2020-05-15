# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:18:08 2020

@author: Kevin Ma
"""

from super_simple_graphics.canvas import *

data = {"Jan":10, "Feb":30, "Mar":50, "Apr":34, "May":70, "Jun":65, 
        "Jul":43, "Aug":89, "Sep":54, "Oct":43, "Nov":52, "Dec":15}

w = 800
h = 800

create_canvas(w,h)
fill_canvas_hsv(50,25,250)

# draw coordinate system
set_font_size(10)
for n in range(10):
    if n>0:
        set_pen_color(160,160,160)
    else:
        set_pen_color(0,0,0)
    draw_static_text(40,100+n*100-5,str(n*100))
    draw_line(80,100+n*100,720,100+n*100)

# draw bar chart
set_brush_color(200,100,100)
total_by_month = []
total_current = 0
i = 0
for key, value in data.items():
    # draw the bars
    set_pen_color(0,0,0,0)
    set_brush_color_hsv(0,180,170,180)
    draw_rect_with_rot_bl(i*50+100,100,45,value,0)
    # draw the month name
    set_pen_color(100,100,100)
    set_font_size(15)
    draw_static_text(i*50+110,80,key)
    # draw the monthly number
    set_font_size(10)
    draw_static_text(i*50+120,102,str(value))
    # calculate the total number by current month
    total_current = total_current + value
    # append it to the list
    total_by_month.append((i*50+125,100 + total_current))
    set_pen_color_hsv(240,180,170,180)
    set_pen_width(6)
    draw_point(i*50+125,100 + total_current)
    draw_static_text(i*50+125,110+total_current,str(total_current))
    # increase the index number by one
    i+=1
    
#draw the curve for total by months
set_pen_width(2)
set_brush_color(0,0,0,0)
set_pen_color_hsv(240,180,170,180)
draw_polyline(total_by_month)

set_font_size(30)
draw_text(w/2,50,400,100,"Car Sales (2020)")

show_canvas()