#!/usr/bin/env python

import time

from envirophat import light, leds


print("""Shows which colours it can see.

Press Ctrl+C to exit.

""")
try:
    leds.on()
    while True:
        r, g, b = light.rgb()


        if r > g and r > b:
          colour = "Red"
        elif g > r and g > b:
          colour = "Green"
        elif b > r and b > g:
          colour = "Blue"
        else:
          colour = "a mix of colours"

        print(str(r) + " Red, " + str(g) + " Green, " + str(b) + " Blue" + " => Is this " + colour + "?")

        time.sleep(1)

except KeyboardInterrupt:
    leds.off()
    pass