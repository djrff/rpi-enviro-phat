#!/usr/bin/env python

import time
import webcolors
from colour import Color
from envirophat import light, leds

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

print("""Shows which colours it can see.

Press Ctrl+C to exit.

""")
try:
    leds.on()
    while True:
        sensor_colour = light.rgb()
        converted_colour = Color(rgb=((sensor_colour[0]/255),(sensor_colour[1]/255),(sensor_colour[2]/255)))
        requested_colour = converted_colour.rgb
        actual_name, closest_name = get_colour_name((requested_colour[0]*255,requested_colour[1]*255,requested_colour[2]*255))

        print("sensor ", sensor_colour, " converted ", converted_colour, " requested ", converted_colour.rgb)
        print "Actual colour name:", actual_name, ", closest colour name:", closest_name

        time.sleep(1)

except KeyboardInterrupt:
    leds.off()
    pass
