#import module geopy

from geopy.geocoders import GeoNames
import json

geolocator = GeoNames(username='YOUR-USERNAME-HERE')  # Register at Geonames

with open('places.csv','r') as f:
    for line in f:
        for word in line.split():
           location = geolocator.geocode(word, timeout=10)
           if location != None:
               json.dumps(location.raw)
               print (word,"\t",location.latitude,",",location.longitude,sep='')
           else:
               print (word)