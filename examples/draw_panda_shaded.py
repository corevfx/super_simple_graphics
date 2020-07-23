import super_simple_graphics.canvas as sg
import random
    
def draw_panda_gradient(x, y):
    sg.set_pen_style('NoPen')
    # ears
    sg.set_brush_style_radial_gradient(x-50, y+95, 40, 120,120,120,0,0,0)
    sg.draw_circle(x-50,y+75,25)
    sg.set_brush_style_radial_gradient(x+50, y+95, 40, 120,120,120,0,0,0)
    sg.draw_circle(x+50,y+75,25)
    # face
    sg.set_brush_style_radial_gradient(x, y+70, 180, 255,255,255,150,150,150)
    sg.draw_circle(x,y,75)
    # eyes
    sg.set_brush_color(0,0,0)
    sg.set_brush_style('SolidPattern')
    sg.draw_ellipse_with_rot(x-30,y-10,50,30,-60)
    sg.draw_ellipse_with_rot(x+30,y-10,50,30,60)
    sg.set_brush_color(255,255,255)
    sg.draw_circle(x-25,y-5,5)
    sg.draw_circle(x+25,y-5,5)
    sg.set_brush_style_radial_gradient(x-27, y-3, 3, 200,200,200,0,0,0)
    sg.draw_circle(x-25,y-5,4)
    sg.set_brush_style_radial_gradient(x+23, y-3, 3, 200,200,200,0,0,0)
    sg.draw_circle(x+25,y-5,4)
    # nose
    sg.set_brush_style_radial_gradient(x-3, y-12, 7, 200,200,200,0,0,0)
    sg.draw_ellipse(x,y-15,20,15)
    # mouth
    sg.set_pen_style('SolidLine')
    sg.set_pen_color(0,0,0)
    sg.set_pen_width(2)
    sg.draw_line(x,y-20,x,y-40)
    sg.draw_elliptical_arc(x,y-30,20,10,180,180)
    
w = 1000
h = 600
num_row = 2
num_col = 4
gapW = w/(num_col+1)
gapH = h/(num_row+1)
sg.create_canvas(w,h)
sg.fill_canvas(200,200,200)
for row in range(num_row):
    for col in range(num_col):
        x = (col+1) * gapW
        y = (row+1) * gapH
        draw_panda_gradient(x,y)
sg.show_canvas()
