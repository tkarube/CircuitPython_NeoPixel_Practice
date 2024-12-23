import time
import board
import neopixel


pixel_pin = board.D18
num_pixels = 100
ORDER = neopixel.GRB
sleepTime = 0.1

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

while True:
    for i in range(0,255,1):
        pixels.fill((0, 0, i))
        pixels.show()
        time.sleep(sleepTime)

    for i in range(255,-1,-1):
        pixels.fill((0, 0, i))
        pixels.show()
        time.sleep(sleepTime)
