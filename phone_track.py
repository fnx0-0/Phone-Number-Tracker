import phonenumbers

import folium

from phonenumbers import geocoder 

Key = '82b12d6a50254454bba865f73221681c'

number=input("Enter the number with country code----->")

samnum = phonenumbers.parse(number)

yourlocation = geocoder.description_for_number(samnum, "en")
print(yourlocation)  #prints the current country of the user of the phone

#for service provider

from phonenumbers import carrier

ser_provider = phonenumbers.parse(number)
print(carrier.name_for_number(ser_provider, "en"))

#using opencage.geocoder for retrieve the coordinates

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourlocation)

results = geocoder.geocode(query)
#print(results)

lat=results[0]['geometry']['lat']

lng=results[0]['geometry']['lng']

print(lat,lng)

mymap = folium.Map(location=[lat,lng], zoom_start = 10)

folium.Marker([lat,lng],popup = yourlocation).add_to((mymap))

## saving map in html
mymap.save("location.html")

