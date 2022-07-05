from unigui import UniGui
from unigui.widget import TextWidget
from unigui.pygamedisplay import PygameDisplay
from adafruit_ili9341 import ILI9341
from unigui.colorscheme import Solarized, VSCode
import displayio
import board
import time

WIDTH = 320
HEIGHT = 240
CS = VSCode.dark

# TODO: Here is where we need to create the object that represents our "display"
# This is the screen where we want our graphical user interface (GUI) to appear.
display_bus = displayio.FourWire(
    board.SPI(),
    command=board.D25,
    chip_select=board.CE0,
    reset=board.D24,
    baudrate=24000000
)
display = ILI9341(display_bus, WIDTH, HEIGHT)

gui = UniGui(WIDTH, HEIGHT, colorscheme=CS)

tw = TextWidget("tw", 0, 0, WIDTH, HEIGHT, colorscheme=CS)
tw.set_value("go gators!")
gui.add_widget(tw)

display.show(gui)

while True:
    display.refresh()
    time.sleep(0.2)
