# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:52:11 2020

@author: Kevin Ma
"""

from super_simple_graphics.canvas import *

w = 1400
h = 800

def demo():
    # demo
    set_pen_color(150,150,150)
    set_pen_width(1)
    draw_grid(w,h)
    
    # set the font for text
    set_font('Helvetica',20)
    
    # draw point
    set_pen_color(200,100,0,150)
    set_pen_width(20)
    draw_point(100,50)
    draw_static_text(200,50,"draw_point")
    
    #draw line 
    set_pen_color(255,155,100)
    set_pen_width(3)
    draw_line(50,125,150,175)
    draw_static_text(200,150,"draw_line")

    #draw rect
    set_pen_width(2)
    set_pen_color(255,0,0)
    set_pen_style(2)
    set_brush_color(150,150,200)
    set_brush_style("HorPattern")
    draw_rect_with_rot(100,250,100,50,10)
    draw_static_text_with_rot(200,250,"draw_rect_with_rot",10)
    
    #draw circle
    set_pen_color(50,150,0)
    set_pen_width(2)
    set_pen_style(3)
    set_brush_color(250,150,100)
    set_brush_style("VerPattern")
    draw_circle(100,350,50)
    draw_static_text(200,350,"draw_circle")
    
    #draw_ellipse_with_rot
    set_pen_color(50,150,200)
    set_pen_width(2)
    set_pen_style(4)
    set_brush_color(150,250,200)
    set_brush_style("Dense3Pattern")
    draw_ellipse_with_rot(100,450,100,70,20)
    draw_static_text_with_rot(200,450,"draw_ellipse_with_rot",10)
    
    #draw pie
    set_pen_width(2)
    set_pen_color(200,10,230)
    set_pen_style(5)
    set_brush_color(200,200,200)
    set_brush_style("CrossPattern")
    draw_pie(100,550,50,30,240)
    draw_static_text(200,550,"draw_pie")
    
    #draw elliptical pie
    set_pen_width(2)
    set_pen_color(100,190,230)
    set_pen_style(1)
    set_brush_color(160,250,230)
    set_brush_style("DiagCrossPattern")
    draw_elliptical_pie(100,650,50,30,60,100)
    draw_static_text(200,650,"draw_elliptical_pie")
    
    #draw arc
    set_pen_width(2)
    set_pen_color(100,190,230)
    set_brush_color(160,250,230)
    draw_arc(100,750,100,80,230)
    draw_static_text(200,750,"draw_arc")
    
    #draw elliptical arc
    set_pen_width(2)
    set_pen_color(100,190,230)
    set_brush_color(160,250,230)
    set_brush_style("CrossPattern")
    draw_elliptical_arc(550,50,50,30,80,230)
    draw_static_text(650,50,"draw_elliptical_arc")
    
    #draw polygon with rot
    points = [(460,130),(530,120),(620,100),(590,200),(540,170),(490,190)]
    set_pen_width(2)
    set_pen_color(255,190,230)
    set_brush_color(160,250,230)
    set_brush_style("VerPattern")
    draw_polygon_with_rot(points, 550,150,10)
    draw_static_text_with_rot(650,150,"draw_polygon_with_rot",10)
    
    #draw path (based on quad bezier)
    points = [(460,230),(530,220),(620,200),(590,300),(540,270),(490,290)]
    set_pen_width(2)
    set_pen_color(100,190,230)
    set_brush_color(230,10,230)
    set_brush_style("HorPattern")
    draw_path(points)
    draw_static_text(650,250,"draw_path")
    
    #draw closed path (based on cubic bezier)
    points = [(460,330),(530,320),(620,300),(590,400),(540,370),(490,390)]
    set_pen_width(2)
    set_pen_color(100,190,230)
    set_brush_color(160,50,30)
    set_brush_style_texture("../images/tile_tex.jpg")
    draw_closed_path(points)
    draw_static_text(650,350,"draw_closed_path")
    
    #draw chord
    set_pen_width(2)
    set_pen_color(100,190,230)
    set_brush_color(160,50,30)
    set_brush_style("NoBrush")
    draw_chord(550,450,50,0,130)
    draw_static_text(650,450,"draw_chord")
    
    #draw elliptical chord
    set_pen_width(2)
    set_pen_color(100,190,230)
    set_brush_color(160,50,30)
    set_brush_style("SolidPattern")
    draw_elliptical_chord(550,550,50,30,0,130)
    draw_static_text(650,550,"draw_elliptical_chord")
    
    #draw rounded rect
    set_pen_width(2)
    set_pen_color(255,100,0)
    set_pen_style(2)
    set_brush_color(150,150,200)
    set_brush_style("HorPattern")
    draw_rounded_rect(550,650,100,50,10,5)
    draw_static_text(650,650,"draw_rounded_rect")
    
    #draw polyline
    points = [(460,730),(530,720),(620,700),(590,800),(540,770),(490,790)]
    set_pen_width(2)
    set_pen_color(100,190,230)
    set_brush_color(230,10,230)
    set_brush_style("HorPattern")
    draw_polyline(points)
    draw_static_text(650,750,"draw_polyline")
    
    #draw rect
    set_pen_width(2)
    set_pen_color(255,0,0)
    set_pen_style(2)
    set_brush_color(150,150,200)
    set_brush_style("HorPattern")
    draw_rect(1000,50,100,50)
    draw_static_text(1100,50,"draw_rect")
    
    #draw_rect_with_rot_tl
    draw_rect_with_rot_tl(1000,150,100,50,10)
    draw_static_text_with_rot(1100,150,"draw_rect_with_rot_tl",10)
    
    #draw_rect_with_rot_bl
    draw_rect_with_rot_bl(1000,250,100,50,10)
    draw_static_text_with_rot(1100,250,"draw_rect_with_rot_bl",10)
    
    #draw_ellipse
    draw_ellipse(1000,350,100,70)
    draw_static_text(1100,350,"draw_ellipse")
    
    #draw_text

    
    #draw_polygon
    points = [(460+450,730),(530+450,720),(620+450,700),(590+450,800),(540+450,770),(490+450,790)]
    draw_polygon(points)
    draw_static_text(1100,750,"draw_polygon")
    

create_canvas(w,h)

demo()

show_canvas()