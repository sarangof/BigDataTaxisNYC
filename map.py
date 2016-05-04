#!/usr/bin/python

import sys
import datetime
import geopandas as gp

zipcodes = gp.read_file('/user/saf537/FinalProject/NYCzipcodeshapefile2.geojson') # ??? How should we import this best?

for line in sys.stdin:
	l = line.strip().split(',') #header condition
        pt_origin = gp.geoseries.Point(float(l[5]),float(l[6])) # column order

	if ((len(l) == 19) & (l[0] != 'VendorID') & (count <= 30)):

	        pt_origin = gp.geoseries.Point(float(l[5]),float(l[6])) # column order
        	pt_destin = gp.geoseries.Point(float(l[9]),float(l[10]))
        	pickup_time = datetime.datetime.strptime(l[1],"%Y-%m-%d %H:%M:%S")
	        dropoff_time = datetime.datetime.strptime(l[2],"%Y-%m-%d %H:%M:%S")
	        c = dropoff_time - pickup_time
        	trip_duration = divmod(c.days * 86400 + c.seconds, 60)

	        for x, z in enumerate(zipcodes['geometry']):
			if pt_origin.intersects(z):
				zip_origin = zipcodes['postalCode'][x]
				break
		for x, z in enumerate(zipcodes['geometry']):
        	        if pt_destin.intersects(z):
				zip_destin = zipcodes['postalCode'][x]
				break
		print "%s|%s\t%d"% (str(zip_origin),str(zip_destin),trip_duration) #Very careful, formatting.


