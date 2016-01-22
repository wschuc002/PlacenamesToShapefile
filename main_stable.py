# Geodetic Engineers of Utrecht
# William Schuch & Rik van Berkum
# Wageningen University and Research
# 22-01-2016

## NOTE BEFORE RUNNING
# Run this line below in the terminal to install the package geopy:
# easy_install geopy
# or:
# pip install geopy

# restart your IDE to perform changes

from twython import Twython
from geopy.geocoders import Nominatim
import json
import datetime
import os
import geopy
import mapnik
import shapefile as shp
import csv

# Setting directory
os.getcwd()
os.chdir("/home/user/git/PlacenamesToShapefile")
os.getcwd()

# Creating output file
dir_output = "./output"
if not os.path.exists(dir_output):
    os.makedirs(dir_output)


## WRITE TO SHAPEFILE
out_file = './output/Places.shp'

#Set up blank lists for data
x,y,city,location=[],[],[],[]

#read data from csv file and store in lists
with open('./data/Placenames_manually.csv', 'rb') as csvfile:
    r = csv.reader(csvfile, delimiter='*')
    for i,row in enumerate(r):
        if i > 0: #skip header
            city.append(row[0])

geolocator = Nominatim()           
for i in city:
    #location.append(geolocator.geocode(str(i))[1])
    x.append(geolocator.geocode(str(i))[1][1])
    y.append(geolocator.geocode(str(i))[1][0])

#Set up shapefile writer and create empty fields
w = shp.Writer(shp.POINT)
w.autoBalance = 1 #ensures gemoetry and attributes match
w.field('X','F',10,8)
w.field('Y','F',10,8)
w.field('City','C',30)
#w.field('Province','C',30)
#w.field('Country','C', 30)

#loop through the data and write the shapefile
for j,k in enumerate(x):
    w.point(k,y[j]) #write the geometry
    w.record(k,y[j],city[j]) #write the attributes

#Save shapefile
w.save(out_file)

def getWKT_PRJ (epsg_code):
 import urllib
 wkt = urllib.urlopen("http://spatialreference.org/ref/epsg/{0}/prettywkt/".format(epsg_code))
 remove_spaces = wkt.read().replace(" ","")
 output = remove_spaces.replace("\n", "")
 return output

# create a projection file
prj = open("./output/Places.prj", "w")
epsg = getWKT_PRJ("4326")
#epsg = getWKT_PRJ("28992")
prj.write(epsg)
prj.close()
