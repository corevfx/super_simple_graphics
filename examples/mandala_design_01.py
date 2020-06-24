# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:08:50 2020

@author: Kevin Ma
"""

import super_simple_graphics.canvas as sg

def design_01():
    num = 80
    sg.set_pen_width(2)
    sg.set_brush_style('NoBrush')
    for i in range(num):
        if i % 4 ==0:
            sg.draw_ellipse(400,0,200,50)
        else:
            sg.draw_ellipse(400,0,150,50)
        sg.rotate_origin(360/num)
        
def design_02():
    # set pen 
    sg.set_pen_color(0,0,0)
    sg.set_pen_style('SolidLine')
    
    # set brush 
    sg.set_brush_style('SolidPattern')
    
    # define points
    away_dist = 350
    points = [(-114,0+away_dist),(-100,40+away_dist),(-20,60+away_dist),(0,100+away_dist),(0,100+away_dist),(20,60+away_dist),(100,40+away_dist),(114,0+away_dist)]
    inner_away_dist = 330
    inner_points = [(-114,10+inner_away_dist),(-100,40+inner_away_dist),(-20,60+inner_away_dist),(0,90+inner_away_dist),(0,90+inner_away_dist),(20,60+inner_away_dist),(100,40+inner_away_dist),(114,10+inner_away_dist)]
    
    # run loop to draw
    num = 10
    for i in range(num):
        # most outer path
        sg.rotate_origin(360/num)
        sg.set_pen_width(4)
        sg.draw_path(points)
        # another path
        sg.set_pen_width(2)
        sg.draw_path(inner_points)
        # dot
        sg.set_pen_width(30)
        sg.draw_point(0,370)
        
    # fill the center with white color
    sg.set_pen_style("NoPen")
    sg.draw_circle(0,0,368)
        
def design_03():
    sg.set_pen_style('SolidLine')
    sg.set_pen_width(5)
    sg.draw_circle(0,0,368)
    sg.set_pen_width(1)
    num = 200
    for i in range(num):
        sg.rotate_origin(360/num)
        sg.draw_line(0,0,368,0)
    sg.set_pen_width(3)
    sg.draw_circle(0,0,340)
    
def design_04():
    num = 20
    # most outer layer
    sg.set_pen_width(2)
    sg.set_brush_color(0,0,0)
    sg.set_brush_style('SolidPattern')
    for i in range(num):
        sg.rotate_origin(360/num)
        sg.draw_ellipse(260,0,150,15)
    sg.set_brush_style('NoBrush')
    sg.rotate_origin(360/num/2)
    
    for i in range(num):
        sg.set_pen_width(2)
        sg.rotate_origin(360/num)
        sg.draw_circle(0,280,40)
        sg.draw_circle(0,280,30)
        sg.set_pen_width(40)
        sg.draw_point(0,280)
        
    # middle layer
    sg.set_brush_style('SolidPattern')
    sg.set_brush_color(255,255,255)
    sg.rotate_origin(360/num/2)
    for i in range(num):
        sg.set_pen_width(2)
        sg.rotate_origin(360/num)
        sg.draw_circle(0,255,37)
        sg.draw_circle(0,255,27)
        sg.set_pen_width(30)
        sg.draw_point(0,255)
        
    # inner layer
    sg.set_brush_style('SolidPattern')
    sg.set_brush_color(255,255,255)
    sg.rotate_origin(360/num/2)
    for i in range(num):
        sg.set_pen_width(2)
        sg.rotate_origin(360/num)
        sg.draw_circle(0,230,37)
        sg.draw_circle(0,230,27)
        
    # cover center
    sg.set_pen_style('NoPen')
    sg.set_brush_color(255,255,255)
    sg.draw_circle(0,0,230)
    
def design_05():
    sg.set_pen_width(2)
    sg.set_pen_style('SolidLine')
    sg.set_pen_color(0,0,0)
    sg.draw_circle(0,0,240)
    sg.draw_circle(0,0,235)
    sg.draw_circle(0,0,215)
    sg.draw_circle(0,0,200)
    num = 200
    sg.set_pen_width(4)
    for i in range(num):
        sg.draw_point(0,207)
        sg.rotate_origin(360/num)
    sg.set_pen_width(5)
    sg.draw_circle(0,0,180)
    
def design_06():
    sg.set_pen_style('NoPen')
    sg.set_brush_style('SolidPattern')
    sg.set_brush_color(0,0,0)
    num = 8
    for i in range(num):
        # draw the 3 leaf grass
        sg.save_stat()
        sg.translate_origin(0,120)
        sg.draw_ellipse(0,25,10,50)
        sg.rotate_origin(-20)
        sg.draw_ellipse(0,25,10,50)
        sg.rotate_origin(40)
        sg.draw_ellipse(0,25,10,50)
        sg.restore_stat()
        # rotate
        sg.rotate_origin(360/num)
    sg.set_brush_style('NoBrush')
    sg.set_pen_style('SolidLine')
    sg.set_pen_width(2)
    sg.rotate_origin(360/num/2)
    for i in range(num):
        sg.draw_rect_with_rot(0,110,65,65,45)
        sg.draw_rect_with_rot(0,100,65,65,45)
        sg.rotate_origin(360/num)
    
# set variables
w = 1100
h = 1100

# create the canvas
sg.create_canvas(w,h)

sg.translate_origin(w/2,h/2)
design_01()

sg.reset_origin()
sg.translate_origin(w/2,h/2)
design_02()

sg.reset_origin()
sg.translate_origin(w/2,h/2)
design_03()

sg.reset_origin()
sg.translate_origin(w/2,h/2)
design_04()

sg.reset_origin()
sg.translate_origin(w/2,h/2)
design_05()

sg.reset_origin()
sg.translate_origin(w/2,h/2)
design_06()

# show the canvas
sg.show_canvas()

