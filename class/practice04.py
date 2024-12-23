import time, random
import myNeoPixel

pixel_pin = 18
num_pixels = 100

pixels = myNeoPixel.Pixels(pixel_pin, num_pixels)
cycler = myNeoPixel.ColroCycler()
sleepSec = 1

while True:
    rgb = cycler.next_rgb()
    pixels.fill(rgb[0], rgb[1], rgb[2])
    time.sleep(sleepSec)

    pixels.fill(0, 0, 0)
    time.sleep(sleepSec)
