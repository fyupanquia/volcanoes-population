import folium
map = folium.Map(location=[38.58,-99.09], zoom_start=6, TileLayer="Map box")

for coordinates in [[38.2,-99.1], [48.2,-100.1]]:
    map.add_child(folium.Marker(location=coordinates, popup="Hi, I'm fyupanquia!", icon=folium.Icon(color="green")))
map.save("map.html")