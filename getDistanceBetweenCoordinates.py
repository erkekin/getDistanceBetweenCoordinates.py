# Copyright (c) 2013 erkekin <erkekin@gmail.com> www.erkekin.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import urllib2
import json
import csv
import sys


def useAPI(csv, writer):
    for row in csv:
        url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=%s+%s&destinations=%s+%s&mode=driving&language=fr-FR&sensor=false" % (
        row[0], row[1], row[2], row[3])

        response = urllib2.urlopen(url)

        from pprint import pprint

        data = json.load(response)
        distance = data['rows'][0]['elements'][0]['distance']['value']

        writer.writerow([row[0], row[1], row[2], row[3], distance])


ofile = open(sys.argv[2], "wb")
writer = csv.writer(ofile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_ALL)

useAPI(csv.reader(open(sys.argv[1], "rb")), writer)

#python request.py points.csv output.csv
