#!/usr/bin/env python
import sys
sys.path.insert(0, '../couchdb')
import socket
hostname = socket.gethostname()

import time
import webcolors
from cloudantclient import client
from envirophat import light, leds

lightdb = client['all-data']

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

def accentuate_colours(colour, average):
    if colour > average:
      return colour + 80
    elif colour < average:
      return colour - 20
    else:
      return colour

print("""Shows which colours it can see.

Press Ctrl+C to exit.

""")
try:
    leds.on()
    while True:
        requested_colour = light.rgb()
        avg = sum(requested_colour)/3
        adjusted_colour = (accentuate_colours(requested_colour[0],avg),accentuate_colours(requested_colour[1],avg),accentuate_colours(requested_colour[2],avg))
        actual_name, closest_name = get_colour_name(adjusted_colour)

        print "Closest colour name:", closest_name, ". RGB", adjusted_colour

        data = {
          "name": hostname,
          "sensor": "colour",
          "created_at": time.strftime("%Y/%m/%d %H:%M:%S +0000", time.gmtime()),
          "light_level": light.light(),
          "led_on": True,
          "colour_name": closest_name,
          "rgb_raw": {
            "red": requested_colour[0],
            "green": requested_colour[1],
            "blue": requested_colour[2]
          },
          "rgb_adjusted": {
            "red": adjusted_colour[0],
            "green": adjusted_colour[1],
            "blue": adjusted_colour[2]
          }
        }

        lightdb.create_document(data)

        time.sleep(1)

except KeyboardInterrupt:
    leds.off()
    pass