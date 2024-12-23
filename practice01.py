import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 30)

# GRB
pixels[0] = (255, 0, 0)
