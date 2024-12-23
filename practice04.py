import time
import board
import neopixel


pixel_pin = board.D18
num_pixels = 100
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

while True:
    for i in range(255):
        pixels.fill((0, 0, i))
        pixels.show()
        time.sleep(0.1)
