getDistance.py
=============

Python script that calculates distance between two decimal degree `(30.123456, 39.123456)` coordinates and outputs it in meters.

###input.csv format 

(coordinates.csv in example)

coordinate1Latitude,coordinate1Longitude,coordinate2Latitude,coordinate2Longitude<br>
coordinate1Latitude,coordinate1Longitude,coordinate2Latitude,coordinate2Longitude<br>
coordinate1Latitude,coordinate1Longitude,coordinate2Latitude,coordinate2Longitude<br>
.....
....
..
###output.csv format 
coordinate1Latitude,coordinate1Longitude,coordinate2Latitude,coordinate2Longitude, DISTANCE IN METERS<br>
coordinate1Latitude,coordinate1Longitude,coordinate2Latitude,coordinate2Longitude, DISTANCE IN METER<br>
coordinate1Latitude,coordinate1Longitude,coordinate2Latitude,coordinate2Longitude, DISTANCE IN METERS<br>
.....<br>
....<br>
..<br>
##Usage
Open console or terminal in project directory <br>
`$ python getDistanceBetweenCoordinates.py coordinates.csv output.csv`

##Google Directions API
https://developers.google.com/maps/documentation/directions/#JSON

##Dev

[@erkekin](http://www.twitter.com/erkekin)
##Licese
 Copyright (c) 2013 erkekin <erkekin at gmail.com> [erkekin.com](http://www.erkekin.com)

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
