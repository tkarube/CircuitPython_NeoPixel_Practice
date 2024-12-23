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

pixels.fill((0, 0, 0))
pixels.show()

while True:
    for i in range(0,num_pixels,1):
        pixels[i] = (0, 255, 0)
        pixels.show()
        time.sleep(sleepTime)

    for i in range(num_pixels-1,0-1,-1):
        pixels[i] = (0, 0, 0)
        pixels.show()
        time.sleep(sleepTime)
