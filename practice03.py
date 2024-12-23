import time
import board
import neopixel


pixel_pin = board.D18
num_pixels = 100
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

print("red")
pixels.fill((0, 255, 0)) # red
pixels.show()
time.sleep(1)

print("green")
pixels.fill((255, 0, 0)) # green
pixels.show()
time.sleep(1)

print("blue")
pixels.fill((0, 0, 255)) # blue
pixels.show()
