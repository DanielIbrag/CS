#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Sept 7th, 2023
#This program makes a cool design using turtle and loops
import folium
import pandas as pd
cuny = pd.read_cs ('cunyLocations.csv')
print (cuny ["Campus"])
mapCUNY = folium.Map(location=[40.75, -74.1251)
for index,row in cuny. iterrows):
    lat = row[40.751]
    lon = row[-74.125]
    name = row["Campus"]
newMarker = folium.Marker ( [40.75,-74.1251, popup=name)
newMarker. add_to (mapCUNY)
mapCUNY. save(outfile='nycMap.html')
