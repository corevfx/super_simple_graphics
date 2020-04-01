# About Super Simple Graphics
Procedural programming style graphics library based on PyQt5 for teaching python programming to designers.
So a lot of the functionalities are provided through global level functions for designers when they just want to create some visuals.
Please check out the example source code in the examples folder, and render results in the images folder.

## How to use the python library:
* Download the simple_graphics.py file and put in the folder where your python files are.
* In your python files, just simply import the functions. 

## Documentation
* Go to Wiki of this project for the documentation
  - [https://github.com/corevfx/super_simple_graphics/wiki](https://github.com/corevfx/super_simple_graphics/wiki)

## Hotkeys when the canvas is shown:
* Press s to save the image to disk.
* Press d to toggle the display overlay layer. Once overlay layer is displayed, Left Mouse Button click on the canvas to show the coordinates of the clicked postion, and Right Mouse Button click to erase all overlay content.
* Press c to show the system color dialog where you can pick a color and see the r,g,b and h,s,v values that you can use in the python coding.
* Press f to show the system font dialog where you can see all the font names, styles and sizes that you can use in the python coding.

### Demo:
Just put below code to run a demo to see most of the graphics functions.
```
# Import all the functions
from super_simple_graphics.canvas import *
# Create the canvas first!
create_win()
# Then call the drawing functions to create graphics
demo()
# In the end, show the canvas!
show_window()
```
The result of demo
![demo](images/demo.jpg)
### More Proper Way of Writing the Demo:
Just put below code to run a demo to see most of the graphics functions.
```
# Import all the functions
import super_simple_graphics.canvas as sg
# Create the canvas first!
sg.create_win()
# Then call the drawing functions to create graphics
sg.demo()
# In the end, show the canvas!
sg.show_window()
```
## Examples:
### Create random circles
![random dots](images/random_points.jpg)
```
import math, random 
from super_simple_graphics.canvas import *

create_win()
for i in range(100):
    set_pen_width(random.random()*200)
    set_pen_color(random.random()*255,0,0,random.random()*255)
    draw_point(i*10, random.random()*800)
show_window()

```
### Create random lines
![random lines](images/random_lines.jpg)
```
import math, random 
from super_simple_graphics.canvas import *

create_win()
for i in range(100):
    set_pen_width(random.random()*50)
    set_pen_color(random.random()*255,0,0,random.random()*255)
    draw_line(i*10, 0, i*10, random.random()*800)
show_window()

```
### For other examples, please look into the examples folder for details.
[Click here for more examples](https://github.com/corevfx/super_simple_graphics/blob/master/examples/readme.md)

### Use for Generative Art


### Use for Graphics Design

### Use for Data Visualization
#### Pie Chart
![pie chart](images/pie_chart.jpg)

#### Bar Chart
![bar chart](images/bar_chart_data_viz.JPG)

## Tools:
### System Color Dialog
![system color dialog](images/system_color_dialog.jpg)

### System Font Dialog
![system font dialog](images/system_font_dialog.jpg)
