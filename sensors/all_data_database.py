#!/usr/bin/env python

import sys
sys.path.insert(0, '/home/pi/djrff/rpi-enviro-phat/sensors')
import light
import motion
import temperature

# import socket
# hostname = socket.gethostname()
# from cloudantclient import client

# try:
#   db = client['your-db-name']
# except:
#   db = client['all-data']

# import time

# from envirophat import light, weather, motion, analog

# unit = 'hPa'  # Pressure unit, can be either hPa (hectopascals) or Pa (pascals)

# def write(line):
#     sys.stdout.write(line)
#     sys.stdout.flush()

# write("--- Writing all data to the database ---")

# try:
#     while True:
#         rgb = light.rgb()
#         mag_values = motion.magnetometer()
#         acc_values = [round(x, 2) for x in motion.accelerometer()]

#         data = {
#           "name": hostname,
#           "sensor": "all data",
#           "created_at": time.strftime("%Y/%m/%d %H:%M:%S +0000", time.gmtime()),
#           "temperature": weather.temperature(),
#           "pressure": weather.pressure(unit=unit),
#           "pressure_unit": unit,
#           "altitude": weather.altitude(), # Supply your local qnh for more accurate readings
#           "light_level": light.light(),
#           "colour_red": rgb[0],
#           "colour_green": rgb[1],
#           "colour_blue": rgb[2],
#           "heading": motion.heading(),
#           "magnetometer_x": mag_values[0],
#           "magnetometer_y": mag_values[1],
#           "magnetometer_z": mag_values[2],
#           "accelerometer_x": acc_values[0],
#           "accelerometer_y": acc_values[1],
#           "accelerometer_z": acc_values[2],
#         }

#         db.create_document(data)

#         time.sleep(1)

# except KeyboardInterrupt:
#     pass
