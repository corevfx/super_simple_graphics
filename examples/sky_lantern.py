import super_simple_graphics.canvas as sg
import math
import random

w = 600
h = 800

# number of points on a sine wave
num = 100
gapH = w/(num-1)

# two mountain HSV colors, one for close up mountain, the other for far away mountain
mountain_blue = [222,231,52]
mountain_blue_far= [222,100,126]

sg.create_canvas(w,h)
# set gradient for the background sky
sg.set_brush_style_linear_gradient(0, 0, 0, h, 115, 108, 122, 30, 20, 41)
# fill the canvas with the gradient 
sg.draw_rect(w/2,h/2,w,h)

def draw_wave(y,color,amp):
    # random offset is for shifting the waves horizontally so they don't look exactly same
    rand_offset = random.random()*4
    # pts is the list of points. Adding two points makes sure sharp corner.
    pts = [(0,0),(0,0)]
    # adding points to the list based on Sine wave
    for i in range(num+1):
        pts.append((i*gapH,y-amp*abs(math.sin(i/5-rand_offset))))
    # adding two points makes sure sharp corner.
    pts.append((w,0))
    pts.append((w,0))
    # no need pen
    sg.set_pen_style('NoPen')
    # set brush hsv color
    sg.set_brush_color_hsv(color[0],color[1],color[2])
    # draw the shape
    sg.draw_closed_path(pts)
    
def draw_sky_lantern(x,y,scale):
    lanternW = 20
    lanternH = 30
    sg.set_brush_style_radial_gradient(x, y-lanternH/2, lanternH, 255, 255, 196, 191, 53, 45)
    sg.draw_rounded_rect(x,y,lanternW*scale,lanternH*scale,5*scale,5*scale)
    
def draw_fg():
    pts = [(0,0),(0,0)]
    for i in range(num+1):
        pts.append((i*gapH,150-5*abs(math.sin(i/5))))
    pts.append((w,0))
    pts.append((w,0))
    sg.set_pen_color(0,0,0)
    sg.set_brush_style('SolidPattern')
    sg.set_brush_color(0,0,0)
    sg.draw_closed_path(pts)
    
def draw_human(x,y):
    sg.set_pen_color(10,10,10)
    sg.set_pen_style('SolidLine')
    sg.set_brush_style('SolidPattern')
    sg.set_brush_color(10,10,10)
    # head
    sg.draw_circle(x,y+100,10)
    # body
    pts = [(x,y+95),(x-30,y+30),(x+10,y+30)]
    sg.draw_polygon(pts)
    # arms and legs    
    sg.set_pen_width(5)
    sg.draw_line(x+5,y+30,x+5,y)
    sg.draw_line(x-5,y+30,x-8,y)
    sg.set_pen_width(4)
    linepts = [(x,y+85),(x+20,y+90),(x+30,y+110)]
    sg.draw_polyline(linepts)
    sg.draw_line(x,y+80,x+40,y+85)

# draw the mountains
sg.set_brush_style('SolidPattern')
num_of_waves = 5
for n in range(num_of_waves):
    new_sat = mountain_blue_far[1] + n*(mountain_blue[1]-mountain_blue_far[1])/num_of_waves
    new_val = mountain_blue_far[2] - n*(mountain_blue_far[2]-mountain_blue[2])/num_of_waves
    new_color = (mountain_blue[0],new_sat,new_val)
    draw_wave(300-n*(n*5),new_color,20)
    
# draw sky lantern, the smaller ones
for t in range(2000):
    draw_sky_lantern(random.randint(0,w),random.randint(100,h),random.uniform(0.1,0.4))
    
# draw sky lanterns, the larger ones
for t in range(200):
    draw_sky_lantern(random.randint(0,w),random.randint(100,h),random.uniform(0.4,1.5))
    
# draw the foreground ground
draw_fg()
# draw the human
draw_human(200,150)

# draw the title
sg.set_pen_width(2)
sg.set_pen_color(255,255,255)
sg.set_font('Chiller',90)
sg.draw_text(w/2,100,w,200,'Sky Lantern')

    
sg.show_canvas()
