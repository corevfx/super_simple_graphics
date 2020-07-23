import super_simple_graphics.canvas as sg

w = 1000
h = 600

sg.create_canvas(w,h)
sg.fill_canvas(200,200,200)

sg.set_pen_style('NoPen')

sg.set_brush_color(180,180,180)
sg.draw_rect(w/2,h/4*3,w,h/2)
sg.set_brush_color(200,200,200)
sg.draw_rect(w/2,h/4,w,h/2)

sg.set_brush_style_linear_gradient(w/2-50, h/2, w/2+80, h/2, 80,80,80, 120,120,120)
sg.draw_ellipse(w/2+50,h/2-95,260,50)

sg.set_brush_style_radial_gradient(w/2-50, h/2+50, 120, 250,250,250,60,60,60)
sg.draw_circle(w/2,h/2,100)

sg.show_canvas()