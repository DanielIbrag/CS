#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Nov 8th 2023
#This program asks for user input then counts the words in the program, finally it counts the number of words that end in s

import folium

mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)
mapCUNY.save(outfile='nycMap.html')