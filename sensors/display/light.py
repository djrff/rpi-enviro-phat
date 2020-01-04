#!/usr/bin/env python
import sys
import time

from envirophat import light, leds

print("""Shows how bright it is, and turns the LEDs on when it's dark.

Press Ctrl+C to exit.

""")

threshold = 0

try:
    while True:
        lightSensor = light.light()
        led = False

        print("{} lumen".format(lightSensor))

        if lightSensor < threshold:
          leds.on()
          led = True
        else:
          leds.off()
          led = False

        time.sleep(0.1)

except KeyboardInterrupt:
    pass