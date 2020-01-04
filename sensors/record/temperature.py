#!/usr/bin/env python
import sys
import socket
import time
sys.path.insert(0, '../../.couchdb')
from cloudantclient import client
from envirophat import weather, leds

hostname = socket.gethostname()

try:
  # For example 'temperature-data'
  db = client['your-db-name'] 
except:
  db = client['all-data']

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
#           leds.on()
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