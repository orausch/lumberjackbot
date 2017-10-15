import time
from array import *
import thread
import sys
from pykeyboard import PyKeyboard
import gtk
k = PyKeyboard()
pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
def get_pixel_rgb(x, y):
    pixbuf.get_from_drawable(gtk.gdk.get_default_root_window(), gtk.gdk.colormap_get_system(), x, y, 0, 0, 1, 1)
    return pixbuf.get_pixels_array()[0][0].tolist()

brown = [161, 116, 56]

def press_l():
    k.press_key(k.left_key)
    k.release_key(k.left_key)
def press_r():
    k.press_key(k.right_key)
    k.release_key(k.right_key)
clicks = array('i',[0,0,0,0,0,0])

# left  = 1
# right = 0
def calculate():
    if get_pixel_rgb(1069, 467) == brown:
        clicks[0] = 1
    else:
        clicks[0] = 0

    if get_pixel_rgb(1069, 402) == brown:
        clicks[1] = 1
    else:
        clicks[1] = 0

    if get_pixel_rgb(1069, 334) == brown:
        clicks[2] = 1
    else:
        clicks[2] = 0
    if get_pixel_rgb(1069, 268) == brown:
        clicks[3] = 1
    else:
        clicks[3] = 0

    if get_pixel_rgb(1069, 200) == brown:
        clicks[4] = 1
    else:
        clicks[4] = 0
         
    if get_pixel_rgb(1073, 135) == brown:
        clicks[5] = 1
    else:
        clicks[5] = 0

def execute():
    delay = 0.015
    for i in clicks:
        if i == 1:
            press_l()
            time.sleep(delay)
            press_l()
        else:
            press_r()
            time.sleep(delay)
            press_r()

time.sleep(2)
press_r()
time.sleep(0.2)
press_r()
while True: 
    time.sleep(0.22)
    calculate()
    execute()
