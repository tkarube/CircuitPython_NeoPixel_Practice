import time, random
import board
import neopixel

pixel_pin = board.D18
num_pixels = 100
ORDER = neopixel.GRB
sleepTime = 1

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

colors = [ [0, 255, 0],
           [255, 0, 0],
           [0, 0, 255] ]

def colorCycle(colors):
    while True:
        for color in colors:
            yield color

colorGenerator = colorCycle(colors)

while True:
    color = next(colorGenerator)
    color = list(color)

    pixels.fill(color)
    pixels.show()
    time.sleep(sleepTime)

    pixels.fill((0, 0, 0)) # turn off all LEDs
    pixels.show()
    time.sleep(sleepTime)
