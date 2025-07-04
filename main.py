import neopixel
from machine import Pin
import time
import random

# Configuration
NUM_LEDS = 108
PIN_NUM = 2
PANEL_SIZE = 54  # Each panel has 54 LEDs

np = neopixel.NeoPixel(Pin(PIN_NUM), NUM_LEDS)

# Colors
WHITE = (255, 255, 255)
OFF = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Helper: Set same pixel on both panels
def set_mirrored(index, color):
    if index < PANEL_SIZE:
        np[index] = color
        np[index + PANEL_SIZE] = color

# Helper: Write changes to strip
def update():
    np.write()

# Fill both panels with same color
def fill_panels(color):
    for i in range(PANEL_SIZE):
        set_mirrored(i, color)
    update()

# Wipe effect on both panels
def color_wipe_panels(color, wait):
    for i in range(PANEL_SIZE):
        set_mirrored(i, color)
        update()
        time.sleep(wait)

# Chase effect on both panels
def chase_panels(color, wait):
    for i in range(PANEL_SIZE):
        set_mirrored(i, color)
        update()
        time.sleep(wait)
        set_mirrored(i, OFF)
    update()

# Sparkle effect on both panels
def sparkle_panels(color, flashes=50, duration=0.02):
    fill_panels(OFF)
    for _ in range(flashes):
        i = random.randint(0, PANEL_SIZE - 1)
        set_mirrored(i, color)
        update()
        time.sleep(duration)
        set_mirrored(i, OFF)
        update()

# Main loop
while True:
    chase_panels(WHITE, 0.02)
    color_wipe_panels(WHITE, 0.02)
#     time.sleep(0.1)
    fill_panels(WHITE)
    time.sleep(2)
#     color_wipe_panels(RED, 0.01)
#     time.sleep(0.5)
# 
#     sparkle_panels(GREEN)
#     time.sleep(1)

    fill_panels(RED)
    time.sleep(4)
    fill_panels(GREEN)
    time.sleep(4)
    fill_panels(OFF)
    time.sleep(1)

