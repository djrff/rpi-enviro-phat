#!/usr/bin/env python

import time

from envirophat import light, leds

print("""Shows how bright it is, and turns the LEDs on when it's dark.

Press Ctrl+C to exit.

""")

threshold = 1000

try:
    while True:
        lightSensor = light.light()

        print("{} lumen".format(lightSensor))

        if lightSensor < threshold:
          leds.on()
        else:
          leds.off()

        time.sleep(0.1)

except KeyboardInterrupt:
    pass