from unigui import UniGui
from unigui.widget import TextWidget
from unigui.pygamedisplay import PygameDisplay
from unigui.colorscheme import Solarized, VSCode
import time

WIDTH = 320
HEIGHT = 240
CS = VSCode.dark

# TODO: Here is where we need to create the object that represents our "display"
# This is the screen where we want our graphical user interface (GUI) to appear.
display = PygameDisplay(WIDTH, HEIGHT)

gui = UniGui(WIDTH, HEIGHT, colorscheme=CS)

tw = TextWidget("tw", 0, 0, WIDTH, HEIGHT, colorscheme=CS)
tw.set_value("hello world!")
gui.add_widget(tw)

display.show(gui)

while True:
    display.refresh()
    time.sleep(0.2)
