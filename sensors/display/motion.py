#!/usr/bin/env python
import sys
import time

from envirophat import motion, leds

print("""This example will detect motion using the accelerometer.
Press Ctrl+C to exit.
""")

threshold = 0.05
readings = []
last_z = 0

try:
    while True:
        motion_detected = False
        last_reading = motion.accelerometer()
        readings.append(last_reading.z)
        readings = readings[-4:]
        z = sum(readings) / len(readings)
        if last_z > 0 and abs(z - last_z) > threshold:
            print("Motion Detected!!!")
            leds.on()
            motion_detected = True

        last_z = z


        time.sleep(0.5)
        leds.off()

except KeyboardInterrupt:
    pass