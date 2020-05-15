# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:37:39 2020

@author: Kevin Ma
"""

import os, sys, functools
from PyQt5 import QtCore, QtGui, QtWidgets

app = None
canvas = None

def callmine(func):
    @functools.wraps(func)
    def w(*args, **kwargs):
        global canvas
        n = func.__name__
        return getattr(canvas,n)(*args,**kwargs)
    return w

def setup(func):
    @functools.wraps(func)
    def w(*args, **kwargs):
        args[0].setup_painter()
        func(*args,**kwargs)
    return w

class CanvasWindow(QtWidgets.QWidget):
    def __init__(self, w=1000, h=800, lb_origin=True, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.w = w
        self.h = h
        self.lb_origin = lb_origin
        self.resize(w,h)
        self.setFixedSize(w,h)
        self.setWindowTitle("Super Simple Graphics - by Kevin Ma")
        
        ## image buffer
        self._main_buffer = QtGui.QPixmap(w,h)
        self._main_buffer.fill()
        ## the main buffer painter
        self.main_buffer_painter = QtGui.QPainter(self._main_buffer)
        self.main_buffer_painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        ## set up pen
        self.pen = QtGui.QPen(QtGui.QColor(0,0,0)) 
        self.pen.setWidth(1)      
        self.pen.setCapStyle(QtCore.Qt.RoundCap)
        self.pen.setJoinStyle(QtCore.Qt.RoundJoin)
        
        ## set up brush
        self.brush = QtGui.QBrush(QtGui.QColor(255,255,255,255))
        self.brush.setStyle(1) # style 1 is SolidPattern
        
        ## overlay buffer
        self._overlay_buffer = QtGui.QPixmap(w,h)
        self._overlay_buffer.fill(QtGui.QColor(0,0,0,0))
        ## the overlay buffer painter
        self.overlay_painter = QtGui.QPainter(self._overlay_buffer)
        self.overlay_painter.setRenderHint(QtGui.QPainter.Antialiasing)
        ## the overlay display toggle
        self.display_overlay = False
        
        ## current buffer and painter
        self.painter = self.main_buffer_painter
        
        ## set up font
        self.font = self.painter.font()
        
        ## fast image access buffer
        self.image_path = ""
        self.image_buffer = None
        
        ## need to set to a new origin
        self._init_coord_sys()
        
    def _init_coord_sys(self):
        if self.lb_origin:
            self.painter.translate(0,self.h)
            self.overlay_painter.translate(0,self.h)
        
    def _set_to_main_buffer_painter(self):
        self.painter = self.main_buffer_painter
        
    def _set_to_overlay_painter(self):
        self.painter = self.overlay_painter
        
    def _draw_coord_overlay(self, x, y):
        self._set_to_overlay_painter()
        set_pen_color(0,0,0)
        set_pen_width(2)
        draw_point(x, y)
        set_font_size(10)
        draw_static_text(x, y, "("+str(x)+","+str(y)+")")
        self._set_to_main_buffer_painter()
    
    def _toggle_display_overlay(self):
        self.display_overlay = not self.display_overlay
        
    def setup_painter(self):
        self.painter.setPen(self.pen)
        self.painter.setBrush(self.brush)
        self.painter.setFont(self.font)
        
    def paintEvent(self, event):
        event_painter = QtGui.QPainter(self)
        event_painter.drawPixmap(0,0,self._main_buffer)
        if self.display_overlay:
            event_painter.drawPixmap(0,0,self._overlay_buffer)
        #event_painter.end()
        
    def mousePressEvent(self, event):
        ### NOTE: The event.pos() will give you the location whose origin is still the top-left corner!
        ###       even though the origin might be moved to other location already !!!
        if event.button() == QtCore.Qt.LeftButton:
            last_point = event.pos()
            x = last_point.x()
            y = last_point.y()
            if self.lb_origin:
                y = self.h-y
            self._draw_coord_overlay(x,y)
        if event.button() == QtCore.Qt.RightButton:
            self._set_to_overlay_painter()
            self._overlay_buffer.fill(QtGui.QColor(0,0,0,0))
            self._set_to_main_buffer_painter()
        self.update()
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_D:
            self._toggle_display_overlay()
        if event.key() == QtCore.Qt.Key_S:
            self.save_image()
        if event.key() == QtCore.Qt.Key_C:
            self.show_color_dialog()
        if event.key() == QtCore.Qt.Key_F:
            self.show_font_dialog()
        self.update()
        
    def save_image(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", "Images (*.jpg)")
        self._main_buffer.save(filename[0])
        
    def show_color_dialog(self):
        QtWidgets.QColorDialog.getColor()
        
    def show_font_dialog(self):
        QtWidgets.QFontDialog.getFont()
                
    def set_pen_width(self, w):
        self.pen.setWidth(w)
        
    def set_pen_color(self, r, g, b, alpha=255):
        self.pen.setColor(QtGui.QColor(r,g,b,alpha))
        
    def set_pen_color_hsv(self, h, s, v, alpha=255):
        c = QtGui.QColor()
        c.setHsv(h,s,v,alpha)
        self.pen.setColor(c)
        
    def set_pen_style(self, style):
        self.pen.setStyle(style)
        
    def set_brush_style(self, style):
        style_dict = get_brush_style_dict()
        s = style_dict.get(style)
        if s is None:
            raise Exception("Can not find brush style '"+str(style)+"'. Please make sure the spelling is correct.")
        self.brush.setStyle(s)
        
    def set_brush_style_linear_gradient(self, x1, y1, x2, y2, r1=0, g1=0, b1=0, r2=255, g2=255, b2=255):
        r = -1 if self.lb_origin else 1
        lg = QtGui.QLinearGradient(x1,r*y1,x2,r*y2)
        lg.setColorAt(0, QtGui.QColor(r1,g1,b1))
        lg.setColorAt(1, QtGui.QColor(r2,g2,b2))
        self.brush = QtGui.QBrush(lg)
        
    def set_brush_style_radial_gradient(self, x, y, radius, r1=0, g1=0, b1=0, r2=255, g2=255, b2=255):
        r = -1 if self.lb_origin else 1
        rg = QtGui.QRadialGradient(x,r*y,radius)
        rg.setColorAt(0, QtGui.QColor(r1,g1,b1))
        rg.setColorAt(1, QtGui.QColor(r2,g2,b2))
        self.brush = QtGui.QBrush(rg)
        
    def set_brush_style_conical_gradient(self, x, y, angle, r1=0, g1=0, b1=0, r2=255, g2=255, b2=255):
        r = -1 if self.lb_origin else 1
        cg = QtGui.QConicalGradient(x,r*y,angle)
        cg.setColorAt(0, QtGui.QColor(r1,g1,b1))
        cg.setColorAt(1, QtGui.QColor(r2,g2,b2))
        self.brush = QtGui.QBrush(cg)
        
    def set_brush_gradient_color_at(self, position, r, g, b):
        # this position is a single float number!
        grad = self.brush.gradient()
        grad.setColorAt(position, QtGui.QColor(r,g,b))
        
    def set_brush_style_texture(self, texture):
        self.brush.setTexture(QtGui.QPixmap(texture))
        
    def set_brush_color(self, r, g, b, alpha=255):
        self.brush.setColor(QtGui.QColor(r,g,b,alpha))
        
    def set_brush_color_hsv(self, h, s, v, alpha=255):
        c = QtGui.QColor()
        c.setHsv(h,s,v,alpha)
        self.brush.setColor(c)
        
    def set_font(self, font_name, font_size):
        self.font.setFamily(font_name)
        self.font.setPixelSize(font_size)
        
    def set_font_size(self, font_size):
        self.font.setPixelSize(font_size)
        
    def set_font_n_style(self, font_name, font_size, font_style):
        database = QtGui.QFontDatabase()
        weight = database.weight(font_name, font_style)
        italic = database.italic(font_name, font_style)
        font = QtGui.QFont(font_name, -1, weight, italic)
        font.setPixelSize(font_size)
        font.setStyleName(font_style)
        self.font = font
        
    def fill_canvas(self, r, g, b, alpha=255):
        if self.lb_origin:
            self.painter.fillRect(0,-self.h,self.w,self.h,QtGui.QColor(r,g,b,alpha))
        else:
            self.painter.fillRect(0,0,self.w,self.h,QtGui.QColor(r,g,b,alpha))
        
    def fill_canvas_hsv(self, h, s, v, alpha=255):
        c = QtGui.QColor()
        c.setHsv(h,s,v,alpha)
        if self.lb_origin:
            self.painter.fillRect(0,-self.h,self.w,self.h,c)
        else:
            self.painter.fillRect(0,0,self.w,self.h,c)
        
    @setup
    def draw_point(self, x, y):
        r = -1 if self.lb_origin else 1
        self.painter.drawPoint(x, r*y)
        
    @setup
    def draw_line(self, x1, y1, x2, y2):
        r = -1 if self.lb_origin else 1
        self.painter.drawLine(x1,r*y1,x2,r*y2)
        
    @setup
    def draw_rect(self, x, y, w, h):
        r = -1 if self.lb_origin else 1
        self.painter.drawRect(x-w/2.0, r*y-h/2.0, w, h)
        
    @setup
    def draw_rect_with_rot(self, x, y, w, h, angle):
        self.save_stat()
        self.translate_origin(x,y)
        self.rotate_origin(angle)
        self.painter.drawRect(0-w/2.0, 0-h/2.0, w, h)
        self.restore_stat()
        
    @setup
    def draw_rect_with_rot_tl(self, x, y, w, h, angle):
        self.save_stat()
        self.translate_origin(x,y)
        self.rotate_origin(angle)
        self.painter.drawRect(0, 0, w, h)
        self.restore_stat()
        
    @setup
    def draw_rect_with_rot_bl(self, x, y, w, h, angle):
        self.save_stat()
        self.translate_origin(x,y)
        self.rotate_origin(angle)
        self.painter.drawRect(0, 0-h, w, h)
        self.restore_stat()
        
    @setup
    def draw_rounded_rect(self, x, y, w, h, x_radius, y_radius):
        r = -1 if self.lb_origin else 1
        self.painter.drawRoundedRect(x-w/2.0,r*y-h/2.0,w,h,x_radius,y_radius)
        
    @setup
    def draw_circle(self, x, y, radius):
        r = -1 if self.lb_origin else 1
        self.painter.drawEllipse(x-radius,r*y-radius,radius*2,radius*2)
        
    @setup
    def draw_ellipse(self, x, y, w, h):
        r = -1 if self.lb_origin else 1
        self.painter.drawEllipse(x-w/2.0,r*y-h/2.0,w,h)
        
    @setup
    def draw_ellipse_with_rot(self, x, y, w, h, angle):
        self.save_stat()
        self.translate_origin(x,y)
        self.rotate_origin(angle)
        # Because the translate_origin() will take lb_origin flag into consideration, 
        # so no need to modify the point coordinates.
        self.painter.drawEllipse(0-w/2.0,0-h/2.0,w,h)
        self.restore_stat()
        
    @setup
    def draw_pie(self, x, y, radius, start_angle, span_angle):
        r = -1 if self.lb_origin else 1
        self.painter.drawPie(x-radius,r*y-radius,radius*2,radius*2,start_angle*16,span_angle*16)
        
    @setup
    def draw_elliptical_pie(self, x, y, x_radius, y_radius, start_angle, span_angle):
        r = -1 if self.lb_origin else 1
        self.painter.drawPie(x-x_radius,r*y-y_radius,x_radius*2,y_radius*2,start_angle*16,span_angle*16)
        
    @setup
    def draw_arc(self, x, y, radius, start_angle, span_angle):
        r = -1 if self.lb_origin else 1
        self.painter.drawArc(x-radius/2.0,r*y-radius/2.0,radius,radius,start_angle*16,span_angle*16)
        
    @setup
    def draw_elliptical_arc(self, x, y, x_radius, y_radius, start_angle, span_angle):
        r = -1 if self.lb_origin else 1
        self.painter.drawArc(x-x_radius,r*y-y_radius,x_radius*2,y_radius*2,start_angle*16,span_angle*16)
        
    @setup
    def draw_chord(self, x, y, radius, start_angle, span_angle):
        r = -1 if self.lb_origin else 1
        self.painter.drawChord(x-radius,r*y-radius,radius*2.0,radius*2.0,start_angle*16,span_angle*16)
        
    @setup
    def draw_elliptical_chord(self, x, y, x_radius, y_radius, start_angle, span_angle):
        r = -1 if self.lb_origin else 1
        self.painter.drawChord(x-x_radius,r*y-y_radius,x_radius*2.0,y_radius*2.0,start_angle*16,span_angle*16)
        
    @setup
    def draw_polygon(self, points):
        polygon = QtGui.QPolygonF() 
        for p in points:
            r = -1 if self.lb_origin else 1
            polygon.append(QtCore.QPointF(p[0], r*p[1]))
        self.painter.drawPolygon(polygon)
        
    @setup
    def draw_polygon_with_rot(self, points, x, y, angle):
        self.save_stat()
        self.translate_origin(x,y)
        self.rotate_origin(angle)
        polygon = QtGui.QPolygonF() 
        for p in points:
            r = -1 if self.lb_origin else 1
            polygon.append(QtCore.QPointF(p[0]-x, r*(p[1] - y)))
        self.painter.drawPolygon(polygon)
        self.restore_stat()
        
    @setup
    def draw_polyline(self, points):
        polyline = QtGui.QPolygonF() 
        for p in points:
            r = -1 if self.lb_origin else 1
            polyline.append(QtCore.QPointF(p[0], r*p[1]))
        self.painter.drawPolyline(polyline)
        
    @setup
    def draw_path(self, points):
        if len(points)<3:
            raise Exception("Only "+len(points)+" points are provided. It needs at least 3 points")
            
        new_pts = [points[0]]
        for i in range(len(points))[1:-2]:
            new_pts.append(points[i])
            mid_pt = ((points[i][0]+points[i+1][0])/2, (points[i][1]+points[i+1][1])/2)
            new_pts.append(mid_pt)
        new_pts.append(points[-2])
        new_pts.append(points[-1])
        path = QtGui.QPainterPath()
        r = -1 if self.lb_origin else 1
        path.moveTo(new_pts[0][0],r*new_pts[0][1])
        for j in range(len(new_pts))[:-1]:
            if j%2 == 1:
                continue
            r = -1 if self.lb_origin else 1
            path.quadTo(new_pts[j+1][0],r*new_pts[j+1][1],new_pts[j+2][0],r*new_pts[j+2][1])
            
        self.painter.drawPath(path)
        
    @setup
    def draw_closed_path(self, points):
        if len(points)<3:
            raise Exception("Only "+len(points)+" points are provided. It needs at least 3 points")
        
        # the first point start from the the first middle point of points[0] and points[1]
        original_first_pt = points[0]
        points[0] = ((points[0][0]+points[1][0])/2, (points[0][1]+points[1][1])/2)
        # to close the path, two more points will be appended
        points.append(original_first_pt)
        points.append(points[0])
            
        new_pts = [points[0]]
        for i in range(len(points))[1:-2]:
            new_pts.append(points[i])
            mid_pt = ((points[i][0]+points[i+1][0])/2, (points[i][1]+points[i+1][1])/2)
            new_pts.append(mid_pt)
        new_pts.append(points[-2])
        new_pts.append(points[-1])
        path = QtGui.QPainterPath()
        r = -1 if self.lb_origin else 1
        path.moveTo(new_pts[0][0],r*new_pts[0][1])
        for j in range(len(new_pts))[:-1]:
            if j%2 == 1:
                continue
            ir = -1 if self.lb_origin else 1
            path.quadTo(new_pts[j+1][0],r*new_pts[j+1][1],new_pts[j+2][0],r*new_pts[j+2][1])
            
        self.painter.drawPath(path)
        
    @setup
    def draw_static_text(self, x, y, text):
        font_size = self.font.pixelSize()
        r = -1 if self.lb_origin else 1
        self.painter.drawStaticText(x,r*y-font_size,QtGui.QStaticText(text))
        
    @setup
    def draw_static_text_with_rot(self, x, y, text, angle):
        self.save_stat()
        self.translate_origin(x,y)
        self.rotate_origin(angle)
        font_size = self.font.pixelSize()
        self.painter.drawStaticText(0,-font_size,QtGui.QStaticText(text))
        self.restore_stat()
    
    @setup
    def draw_text(self, x, y, w, h, text):
        # not
        r = -1 if self.lb_origin else 1
        self.painter.drawText(QtCore.QRect(x-w/2.0,r*y-h/2.0,w,h),QtCore.Qt.AlignCenter,text)
        
    def draw_image(self, x, y, sx, sy, sw, sh, image_path):
        # not
        image = QtGui.QImage(image_path)
        r = -1 if self.lb_origin else 1
        self.painter.drawImage(x,r*y,image,sx,sy,sw,sh)
        
    def set_buffer_image(self,image_path):
        # not
        p = os.path.abspath(image_path)
        if not os.path.isfile(p):
            raise Exception("The image specified '"+p+"' does not exist!")
        if p is not self.image_path:
            self.image_path = p
            self.image_buffer = QtGui.QImage(p)
        
    def get_color_from_buffer_image(self, x, y):
        # not
        r = -1 if self.lb_origin else 1
        color = self.image_buffer.pixelColor(x,r*y)
        result =(color.red(), color.green(), color.blue())
        return result
    
    def save_stat(self):
        self.painter.save()
        
    def restore_stat(self):
        self.painter.restore()
        
    def reset_origin(self):
        self.painter.resetTransform()
        self._init_coord_sys()
        
    def translate_origin(self, x, y):
        r = -1 if self.lb_origin else 1
        self.painter.translate(x,r*y)
        
    def rotate_origin(self, d):
        self.painter.rotate(d)
        
    def scale_origin(self, sx, sy):
        self.painter.scale(sx, sy)

        
def create_canvas(w=1000,h=800):
    """
    Creates a windows with given width and height.
    
    :param w: The width of the window.
    :type w: int, defaults to 1000
    :param h: The height of the window.
    :type h: int, defaults to 600
    """
    global app, canvas
    app = QtWidgets.QApplication(sys.argv)
    canvas = CanvasWindow(w,h)

def show_canvas():
    """
    Shows the window that was created previously using create_win() function.
    """
    canvas.show()
    
    app.exec_()
    canvas.main_buffer_painter.end()
    canvas.overlay_painter.end()
    #sys.exit(app.exec_())
      
@callmine
def set_pen_width(w):
    """
    Set pen width to the given value.
    
    :param w: The pen width.
    :type w: int
    """
    pass

@callmine
def set_pen_style(style):
    """
    Sets the pen style.
    
    :param style: The string representation of the following pen styles: 
        "NoPen", 
        "SolidLine", 
        "DashLine", 
        "DotLine", 
        "DashDotLine", 
        "DashDotDotLine".
    :type style: string
    """
    
@callmine
def set_pen_color(r, g, b, alpha=255):
    """
    Sets the pen color to a color defined by r, g, b, alpha.
    Pen is used to draw the outline of the shape.
    The value range of r, g, b, or alpha is 0 - 255. 
    0 is black and 255 is white.
    
    :param r: The red component of the color.
    :type r: int
    :param g: The green component of the color.
    :type g: int
    :param b: The blue component of the color.
    :type b: int
    :param alpha: The alpha channel of a color.
    :type alpha: int, defaults to 255
    """
    pass

@callmine
def set_pen_color_hsv(h, s, v, alpha=255):
    """
    Sets the pen color to a color defined by h, s, v, alpha.
    Pen is used to draw the outline of the shape.
    HSV stands for Hue, Saturation, Value
    h is in the range 0 - 359. Red is 0, yellow is 60, green is 120, cyan is 180, blue is 240, pink is 300.
    s is in the range 0 - 255.
    v is in the range 0 - 255.
    
    :param h: The hue of the color.
    :type h: int
    :param s: The saturation of the color.
    :type s: int
    :param v: The value of the color.
    :type v: int
    :param alpha: The alpha channel of a color.
    :type alpha: int, defaults to 255
    """
    pass

@callmine
def set_brush_style(style):
    """
    Sets the brush style to the following patterns:
        "NoBrush", "SolidPattern", "Dense1Pattern", "Dense2Pattern", "Dense3Pattern", "Dense4Pattern",
        "Dense5Pattern", "Dense6Pattern", "Dense7Pattern", "HorPattern", "VerPattern", "CrossPattern",
        "BDiagPattern", "FDiagPattern", "DiagCrossPattern".

    Please Note. For other patterns, please call corresponding functions provided.
        LinearGradientPattern  -> set_brush_style_linear_gradient()
        RadialGradientPattern -> set_brush_style_radial_gradient()
        ConicalGradientPattern -> set_brush_style_conical_gradient()
        TexturePattern -> set_brush_style_texture()
        
    :param style: The brush style.
    :type style: string
    """
    pass

@callmine
def set_brush_style_linear_gradient(x1, y1, x2, y2, r1=0, g1=0, b1=0, r2=255, g2=255, b2=255):
    """
    Sets brush style to linear gradient with interpolation area between (x1, y1) and (x2, y2) and interpolation color 
    between (r1,g1,b1) and (r2,g2,b2).
    
    :param x1: The x coordinate of the start point of the gradient.
    :type x1: int
    :param y1: The y coordinate of the start point of the gradient.
    :type y1: int
    :param x2: The x coordinate of the end point of the gradient.
    :type x2: int
    :param y2: The y coordinate of the end point of the gradient.
    :type y2: int
    :param r1: The red component of the start color of the gradient.
    :type r1: int
    :param g1: The green component of the start color of the gradient.
    :type g1: int
    :param b1: The blue component of the start color of the gradient.
    :type b1: int
    :param r2: The red component of the end color of the gradient.
    :type r2: int
    :param g2: The green component of the end color of the gradient.
    :type g2: int
    :param b2: The blue component of the end color of the gradient.
    :type b2: int
    """
    pass

@callmine
def set_brush_style_radial_gradient(x, y, radius, r1=0, g1=0, b1=0, r2=255, g2=255, b2=255):
    """
    Sets brush style to radial gradient with interpolation area between centre (x1, y1) and position that is radius distance away from centre
    and interpolation color between (r1,g1,b1) and (r2,g2,b2).
    """
    pass

@callmine
def set_brush_style_conical_gradient(x, y, angle, r1=0, g1=0, b1=0, r2=255, g2=255, b2=255):
    """
    Sets brush style to conical gradient with the given center (cx, cy), starting the interpolation at the given angle. 
    The angle must be specified in degrees between 0 and 360.
    Interpolation color is between (r1,g1,b1) and (r2,g2,b2).
    """
    pass

@callmine
def set_brush_gradient_color_at(position, r, g, b):
    """
    This function must be used AFTER either one of the three functions is used:
        set_brush_style_linear_gradient(), set_brush_style_radial_gradient() or set_brush_style_conical_gradient()
    Position value must be in the range of (0-1). 0 meaning the start of the gradient, 1 meaning the end of the gradient.
    """
    pass

@callmine
def set_brush_style_texture(texture):
    """
    Sets brush pixmap to texture. 
    
    :param texture: The path to a texture image file.
    :type texture: string
    """
    pass
    
@callmine
def set_brush_color(r, g, b, alpha=255):
    """
    Sets the brush color to a color defined by r, g, b, alpha.
    Brush is used to fill the shapes.
    r, g, b, or alpha value range is 0 - 255
    """
    pass

@callmine
def set_brush_color_hsv(h, s, v, alpha=255):
    """
    Sets the brush color to a color defined by h, s, v, alpha.
    Brush is used to fill the shapes.
    HSV stands for Hue, Saturation, Value
    h is in the range 0 - 359. Red is 0, yellow is 60, green is 120, cyan is 180, blue is 240, pink is 300.
    s is in the range 0 - 255.
    v is in the range 0 - 255.
    """
    pass

@callmine
def set_font(font_name, font_size):
    """
    Set the font name and size (in pixels).
    Example, set_font("Helvatica", 42)
    In the tools folder, there is a tool (display_fonts.py) can be used to see 
    all available fonts on your current Operating System. 
    """
    pass

@callmine
def set_font_size(font_size):
    """
    Set the font size (in pixels).
    Example, set_font(42)
    In the tools folder, there is a tool (display_fonts.py) can be used to see 
    all available fonts on your current Operating System. 
    """
    pass

@callmine
def set_font_n_style(font_name, font_size, font_style):
    """
    Set the font name, size (in pixels), and style.
    Example, set_font("Arial", 42, "Bold Italic")
    In the tools folder, there is a tool (display_fonts.py) can be used to see 
    all available fonts on your current Operating System. 
    """
    pass

@callmine
def fill_canvas(r, g, b, alpha=255):
    """
    Fill the canvas with color defined by r, g, b, alpha
    """
    pass

@callmine
def fill_canvas_hsv(h, s, v, alpha=255):
    """
    Fill the canvas with color defined by h, s, v, alpha.
    HSV stands for Hue, Saturation, Value
    h is in the range 0 - 359. Red is 0, yellow is 60, green is 120, cyan is 180, blue is 240, pink is 300.
    s is in the range 0 - 255.
    v is in the range 0 - 255.
    """
    pass

@callmine
def draw_point(x, y):
    """
    Draws a single point at position (x, y).
    """
    pass

@callmine
def draw_line(x1, y1, x2, y2):
    """
    Draws a line from (x1, y1) to (x2, y2).
    """
    pass

@callmine
def draw_rect(x,y,w,h):
    """
    Draws a rectangle with centre at (x, y) and with the given width and height.
    """
    pass

@callmine
def draw_rect_with_rot(x,y,w,h,angle):
    """
    Draws a rectangle with centre at (x, y), with the given width and height and with rotation around centre.
    Rotation is in degrees and clock wise direction.
    """
    pass

@callmine
def draw_rect_with_rot_tl(x,y,w,h,angle):
    """
    Draws a rectangle with top left corner at (x, y), with the given width and height and with rotation around centre.
    Rotation is in degrees and clock wise direction.
    """
    pass

@callmine
def draw_rect_with_rot_bl(x,y,w,h,angle):
    """
    Draws a rectangle with bottom left corner at (x, y), with the given width and height and with rotation around centre.
    Rotation is in degrees and clock wise direction.
    """
    pass

@callmine
def draw_rounded_rect(x, y, w, h, x_radius, y_radius):
    """
    Draws the given rectangle defined by centre (x, y), w (width), h (height), with rounded corners.
    The x_radius and y_radius arguments specify the radii of the ellipses defining the corners of the rounded rectangle.
    """
    pass

@callmine
def draw_static_text(x,y,text):
    """
    Draws the staticText at coordinates x (left) and y (top).
    """
    pass

@callmine
def draw_static_text_with_rot(x,y,text,angle):
    """
    Draws the staticText at coordinates x (left) and y (top) with rotation around the top left corner.
    """
    pass

@callmine
def draw_text(x, y, w, h, text):
    """
    Draws the given text within the provided rectangle defined by centre (x, y), width w, and height h.
    """

@callmine
def draw_circle(x,y,radius):
    """
    Draws the circle defined by the centre at (x, y) and the radius.
    """
    pass

@callmine
def draw_ellipse(x,y,w,h):
    """
    Draws the ellipse defined by the centre at (x, y) with the given width and height.
    """
    pass

@callmine
def draw_ellipse_with_rot(x,y,w,h,angle):
    """
    Draws the ellipse defined by the centre at (x, y), with the given width and height and with rotation around centre.
    Rotation is in degrees and clock wise direction.
    """
    pass

@callmine
def draw_pie(x,y,radius,start_angle,span_angle):
    '''
    Draws the pie defined by the centre at (x, y) 
    with the specified radius, and the given start_angle and span_angle.
    Zero degree for start_angle is at 3 o'clock.
    '''
    pass

@callmine
def draw_elliptical_pie(x,y,x_radius,y_radius,start_angle,span_angle):
    '''
    Draws the pie defined by the square beginning at (x, y) 
    with the specified x radius and y radius of the ellipse, and the given start_angle and span_angle.
    Zero degree for start_angle is at 3 o'clock.
    '''
    pass

@callmine
def draw_arc(x,y,radius,start_angle,span_angle):
    """
    Draws the arc defined by the centre at (x, y) 
    with the specified radius, and the given startAngle and spanAngle.
    """
    pass

@callmine
def draw_elliptical_arc(x,y,x_radius,y_radius,start_angle,span_angle):
    """
    Draws the arc defined by the centre at (x, y) 
    with the specified x radius and y radius of the ellipse, and the given startAngle and spanAngle.
    Zero degree for start_angle is at 3 o'clock.
    """
    pass

@callmine
def draw_chord(x,y,radius,start_angle,span_angle):
    """
    Draws the chord defined by the centre at (x, y) 
    with the specified radius, and the given startAngle and spanAngle.
    Zero degree for start_angle is at 3 o'clock.
    """
    pass

@callmine
def draw_elliptical_chord(x,y,x_radius,y_radius,start_angle,span_angle):
    """
    Draws the chord defined by the centre at (x, y) 
    with the specified x radius and y radius of the ellipse, and the given startAngle and spanAngle.
    Zero degree for start_angle is at 3 o'clock.
    """
    pass

@callmine
def draw_polygon(points):
    """
    Draws the polygon defined by the points in the list points using the 
    current pen and brush. The first point is implicitly connected to the last point, 
    and the polygon is filled with the current brush.
    
    :param points: The points is a list of tuples specifying the points' positions. 
    :type points: list of tuples. Example, [(1,5),(200.7,40),(23,45.0)]
    """
    pass

@callmine
def draw_polygon_with_rot(points, x, y, angle):
    """
    Draws the polygon defined by the points in the list points with the rotation defined by
    angle and rotation pivot point at (x, y). The first point is implicitly connected to the 
    last point, and the polygon is filled with the current brush.
    
    :param points: The points is a list of tuples specifying the points' positions. 
    :type points: list of tuples. Example, [(1,5),(200.7,40),(23,45.0)]
    :param x: X coordinate of the rotation pivot point.
    :type x: int
    :param y: Y coordinate of the rotation pivot point.
    :type y: int
    :param angle: The rotation angle in degrees. Positive angle rotation is clockwise.
    :type angle: int. In the range of 0-360.
    """
    pass

@callmine
def draw_polyline(points):
    """
    Draws the polyline defined by the given points. Note it won't be filled with brush.
    
    :param points: The points is a list of tuples specifying the points' positions. 
    :type points: list of tuples. Example, [(1,5),(200.7,40),(23,45.0)]
    """
    pass

@callmine
def draw_path(points):
    """
    Draws the path defined by the control points in the list points. 
    
    :param points: The points is a list of tuples specifying the control points' positions. 
    :type points: list of tuples. Example, [(1,5),(200.7,40),(23,45.0)]
    """
    pass

@callmine
def draw_closed_path(points):
    """
    Draws the path defined by the control points in the list points. 
    The first point is implicitly connected to the last point, and 
    the polygon is filled with the current brush.
    
    :param points: The points is a list of tuples specifying the control points' positions. 
    :type points: list of tuples. Example, [(1,5),(200.7,40),(23,45.0)]
    """
    pass

@callmine
def draw_image(x, y, sx, sy, sw, sh, image_path):
    """
    Draws an image at (x, y) by copying a part of image into the paint device.
    (x, y) specifies the top-left point in the paint device that is to be drawn onto. 
    (sx, sy) specifies the top-left point in image that is to be drawn. The default is (0, 0).
    (sw, sh) specifies the size of the image that is to be drawn. 
    The default, (0, 0) (and negative) means all the way to the bottom-right of the image.
    """
    pass

@callmine
def get_color_from_buffer_image(x, y):
    """
    Gets the rgb color from the buffer image at position x and y. 
    X and y are the horizontal and vertical pixel values.
    The returned value is a tuple of 3 components (r,g,b).
    NOTE: 
        Please use set_buffer_image(image_path) to set buffer image first before 
        accessing the image pixel information.
    """
    pass

@callmine
def set_buffer_image(image_path):
    """
    Sets the buffer image to an image file specified by the image_path. 
    """
    pass

@callmine
def save_stat():
    pass

@callmine
def restore_stat():
    pass

@callmine
def reset_origin():
    pass

@callmine
def translate_origin():
    pass

@callmine
def rotate_origin():
    pass

@callmine
def scale_origin(sx, sy):
    pass

def get_brush_style_dict():
    result = {}
    for key in dir(QtCore.Qt):
        value = getattr(QtCore.Qt, key)
        if isinstance(value, QtCore.Qt.BrushStyle):
            result[key] = value
            result[value] = key
    return result

def draw_grid(w=1000,h=800,spacing=50):
    """
    Draws the grid in the rectangle defined by w and h.
    And the spacing distance between grid lines is specified by spacing.
    """
    for i in range(0,w+1,spacing):
        draw_line(i,0,i,h)
    for j in range(0,h+1,spacing):
        draw_line(0,j,w,j)