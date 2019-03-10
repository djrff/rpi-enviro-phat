#!/usr/bin/env python
import sys
sys.path.insert(0, '../couchdb')
import socket
hostname = socket.gethostname()
from cloudantclient import client

db = client['all-data']

import time

from envirophat import motion, leds


print("""This example will detect motion using the accelerometer.
Press Ctrl+C to exit.
""")

threshold = 0.2
readings = []
last_z = 0

try:
    while True:
        readings.append(motion.accelerometer().z)
        readings = readings[-4:]
        z = sum(readings) / len(readings)
        if last_z > 0 and abs(z - last_z) > threshold:
            print("Motion Detected!!!")
            leds.on()
                data = {
                    "name": hostname,
                    "sensor": "motion",
                    "created_at": time.strftime("%Y/%m/%d %H:%M:%S +0000", time.gmtime()),
                    "threshold": threshold,
                    "last_z": last_z,
                    "z": z,
                    "readings": readings
                }

            db.create_document(data)
        last_z = z


        time.sleep(0.01)
        leds.off()

except KeyboardInterrupt:
    pass