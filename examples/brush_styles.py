# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:07:35 2020

@author: MAYI
"""

import math, random 
from super_simple_graphics.canvas import *

create_win(1000,800)
fill_canvas_hsv(50,25,250)

set_brush_color(200,100,100)

for i in range(0, 25):
    centre_x = (i%5)*200+100
    centre_y = int(i/5)*150+100
    bsd = get_brush_style_dict()
    style = bsd.get(i)
    if not style:
        continue
    set_brush_style(style)
    if style == "LinearGradientPattern":
        set_brush_style_linear_gradient(centre_x-50,centre_y,centre_x+50,centre_y,255,0,0,0,0,255)
    if style == "RadialGradientPattern":
        set_brush_style_radial_gradient(centre_x, centre_y, 50, 255,0,0,0,0,255)
    if style == "ConicalGradientPattern":
        set_brush_style_conical_gradient(centre_x, centre_y, 20, 255,0,0,0,0,255)
    if style == "TexturePattern":
        set_brush_style_texture("../images/tile_tex.jpg")
    draw_rect(centre_x, centre_y, 100, 100)
    draw_text(centre_x, centre_y+60, 200, 100, style)


show_window()