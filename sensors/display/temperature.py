#!/usr/bin/env python
import sys
import time

from envirophat import weather, leds

print("""Light the LEDs upon temperature increase.

Press Ctrl+C to exit.

""")

threshold = None

try:
    while True:
        temperature = weather.temperature()
        led = False

        if threshold is None:
            threshold = temperature + 2

        print("{} degrees Celsius".format(temperature))
        if temperature > threshold:
            leds.on()
            led = True
        else:
            leds.off()
            led = False

        time.sleep(0.1)

except KeyboardInterrupt:
    pass