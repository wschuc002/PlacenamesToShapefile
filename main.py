# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 09:21:06 2016

@author: user
"""
# Run this line below in the terminal to install the package geopy:
# easy_install geopy
# or:
# pip install geopy

# restart your IDE to dgdfgdf changes

from twython import Twython
import json
import datetime
import os
import geopy

import mapnik

os.getcwd()
os.chdir("/home/user/git/PlacenamesToShapefile")
os.getcwd()



from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("Wageningen")
print(location.address)

print((location.latitude, location.longitude))
