import urllib2
import json
import csv
import sys

def useAPI(csv, writer):

	for row in csv:    
		
		url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=%s+%s&destinations=%s+%s&mode=driving&language=fr-FR&sensor=false" % (row[0],row[1],row[2],row[3])

		response = urllib2.urlopen(url)
		
		from pprint import pprint

		data =json.load(response)
		distance= data['rows'][0]['elements'][0]['distance']['value']

		writer.writerow([row[0],row[1],row[2],row[3], distance])


ofile  = open(sys.argv[2], "wb")
writer = csv.writer(ofile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_ALL)

useAPI(csv.reader(open(sys.argv[1],"rb")),writer)

#python request.py points.csv output.csv
