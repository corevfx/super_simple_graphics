import super_simple_graphics.canvas as sg
import random

w=1800
h=600
sg.create_canvas(w,h)
sg.fill_canvas(164,236,255)

def draw_many_circles(num):
    sg.set_pen_style('NoPen')
    for i in range(num):
        width = random.randint(0,200)
        x = random.randint(0,w)
        y = random.randint(0,h)
        sg.set_brush_style_linear_gradient(x-width/2,y,x+width/2,y,255,(num-i)/num*200,(num-i)/num*200,255,255,255)
        sg.draw_circle(x,y,width/2)

draw_many_circles(200)

sg.set_brush_style('SolidPattern')
sg.set_brush_color(255,0,0,120)
sg.draw_rect(w/2,197,w,110)

sg.set_font('Kozuka Gothic Pr6N EL',120)
sg.set_pen_style('SolidLine')
sg.set_pen_color(255,255,255)
sg.draw_static_text(100,200,"BALLOONS")


sg.show_canvas()