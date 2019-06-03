#!/usr/bin/env python
import sys
sys.path.insert(0, '/home/pi/djrff/rpi-enviro-phat/couchdb')
import socket
hostname = socket.gethostname()
from cloudantclient import client

try:
  db = client['your-db-name']
except:
  db = client['motion-data']

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

        data = {
            "name": hostname,
            "sensor": "motion",
            "created_at": time.strftime("%Y/%m/%d %H:%M:%S +0000", time.gmtime()),
            "threshold": threshold,
            "motion_detected": motion_detected,
            "last_z": last_z,
            "average_z": z,
            "z": last_reading.z,
            "x": last_reading.x,
            "y": last_reading.y,
            "z_readings": readings
        }

        db.create_document(data)

        last_z = z


        time.sleep(0.5)
        leds.off()

except KeyboardInterrupt:
    pass