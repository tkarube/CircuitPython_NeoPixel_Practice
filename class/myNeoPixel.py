import time, random
import board
import neopixel

class Pixels:
    def __init__(self, num_pin, num_pixels):

        pixel_pin = pixel_pin = getattr(board, f'D{num_pin}')
        self.pixel_pin = pixel_pin,
        self.num_pixels = num_pixels

        ORDER = neopixel.GRB

        self.pixels = neopixel.NeoPixel(
            pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
        )

        # turn off all LEDs
        self.pixels.fill((0, 0, 0))
        self.pixels.show()
 
    def fill(self, green, red, blue):
        self.pixels.fill((green, red, blue))
        self.pixels.show()

    def lightUp(self, pos, green, red, blue):
        self.pixels[pos] = (green, red, blue)
        self.pixels.show()

class ColroCycler:
    def __init__(self):

        self.rgb = [ [0, 255, 0],
                     [255, 0, 0],
                     [0, 0, 255] ]
        self.index = 0

    def next_rgb(self):
        rgb = self.rgb[self.index]
        self.index = (self.index + 1) % len(self.rgb)
        return rgb
