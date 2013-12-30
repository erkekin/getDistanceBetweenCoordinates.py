getDistance.py
=============

Python script that calculates distance between two decimal degree (30.123456, 39.123456) coordinates and outputs it in meters.

#input.csv format 

(coordinates.csv in example)

coordinate1Latitude,coordinate1Longitude,coordinate2Latitude,coordinate2Longitude
coordinate1Latitude,coordinate1Longitude,coordinate2Latitude,coordinate2Longitude
coordinate1Latitude,coordinate1Longitude,coordinate2Latitude,coordinate2Longitude
.....
....
..
#output.csv format 
coordinate1Latitude,coordinate1Longitude,coordinate2Latitude,coordinate2Longitude, DISTANCE IN METERS
coordinate1Latitude,coordinate1Longitude,coordinate2Latitude,coordinate2Longitude, DISTANCE IN METERS
coordinate1Latitude,coordinate1Longitude,coordinate2Latitude,coordinate2Longitude, DISTANCE IN METERS
.....
....
..
#Usage
$ python getDistanceBetweenCoordinates.py coordinates.csv output.csv

#Google Directions API
https://developers.google.com/maps/documentation/directions/#JSON
#Dev
@erkekin
