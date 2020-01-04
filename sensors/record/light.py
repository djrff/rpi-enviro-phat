#!/usr/bin/env python
import sys
import socket
import time
sys.path.insert(0, '../../.couchdb')
from cloudantclient import client

hostname = socket.gethostname()

try:
  # For example 'light-data'
  db = client['your-db-name']
except:
  db = client['all-data']


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
#         leds.on()
          led = True
        else:
          leds.off()
          led = False

        data = {
          "name": hostname,
          "sensor": "light",
          "created_at": time.strftime("%Y/%m/%d %H:%M:%S +0000", time.gmtime()),
          "light_level": light.light(),
          "led_on": led,
        }

        db.create_document(data)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass