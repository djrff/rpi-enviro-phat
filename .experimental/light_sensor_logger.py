import sys
sys.path.insert(0, '../couchdb')

from cloudantclient import client
import time
from envirophat import light, leds

lightdb = client['light-sensor']

#for document in lightdb:
#  print(document)

try:
    while True:
      leds.on()
      r,g,b = light.rgb()
      leds.off()

      data = {
        "name": "djrff-rpi-1",
        "created_at": time.strftime("%Y/%m/%d %H:%M:%S +0000", time.gmtime()),
        "light_level": light.light(),
        "led_on": True,
        "rgb": {
          "red": r,
          "green": g,
          "blue": b
        }
      }

      lightdb.create_document(data)
      print(data['created_at'], " - data submitted - ", data['light_level'])
      time.sleep(1)

except KeyboardInterrupt:
    leds.off()

def __exit__(self, exc_type, exc_value, traceback):
    leds.off()
