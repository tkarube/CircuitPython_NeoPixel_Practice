import time, random
import board
import neopixel

pixel_pin = board.D18
num_pixels = 100
ORDER = neopixel.GRB
sleepTime = 0.1 # changed in the loop between 0.01 - 0.1

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

pixels.fill((0, 0, 0))
pixels.show()

while True:
    sleepTime = random.random() * 0.1
    print(sleepTime)
    for i in range(0,num_pixels,1):
        pixels[i] = (0, 255, 0)
        pixels.show()
        time.sleep(sleepTime)

    sleepTime = random.random() * 0.1
    print(sleepTime)
    for i in range(0,num_pixels,1):
        pixels[i] = (255, 0, 0)
        pixels.show()
        time.sleep(sleepTime)

    sleepTime = random.random() * 0.1
    print(sleepTime)
    for i in range(0,num_pixels,1):
        pixels[i] = (0, 0, 255)
        pixels.show()
        time.sleep(sleepTime)

    sleepTime = random.random() * 0.1
    print(sleepTime)
    for i in range(0,num_pixels,1):
        pixels[i] = (0, 0, 0)
        pixels.show()
        time.sleep(sleepTime)
