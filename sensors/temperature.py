#!/usr/bin/env python
import sys
sys.path.insert(0, '/home/pi/djrff/rpi-enviro-phat/couchdb')
import socket
hostname = socket.gethostname()
from cloudantclient import client

try:
  db = client['your-db-name']
except:
  db = client['temperature-data']

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

        data = {
          "name": hostname,
          "sensor": "temperature",
          "created_at": time.strftime("%Y/%m/%d %H:%M:%S +0000", time.gmtime()),
          "threshold": threshold,
          "temperature": temperature,
          "led_on": led
        }

        db.create_document(data)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass