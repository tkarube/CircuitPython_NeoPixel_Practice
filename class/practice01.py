import time, random
import myNeoPixel

pixel_pin = 18
num_pixels = 100

pixels = myNeoPixel.Pixels(pixel_pin, num_pixels)
pixels.fill(255, 0, 0)
