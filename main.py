import folium
import pandas

map = folium.Map(location = [51.5073219, -0.1276474], zoom_start = 10, tiles = "Stamen Terrain")
data = pandas.read_csv('volcano.csv')
fg = folium.FeatureGroup(name="My Map")

coords = list(zip(list(data['LAT']), list(data['LON'])))

for i in coords:
    fg.add_child(folium.Marker(location = i, popup="VOLCANO", icon=folium.Icon(color="red")))

map.add_child(fg)
map.save("Map.html")
