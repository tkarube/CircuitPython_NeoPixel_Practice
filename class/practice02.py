import time, random
import myNeoPixel

pixel_pin = 18
num_pixels = 100

pixels = myNeoPixel.Pixels(pixel_pin, num_pixels)

rgbList = [ [0, 255, 0],
            [255, 0, 0],
            [0, 0, 255] ]

while True:
    for n in range(3):
        pixels.fill(rgbList[n][0], rgbList[n][1], rgbList[n][2])
        time.sleep(1)

        pixels.fill(0, 0, 0)
        time.sleep(1)
