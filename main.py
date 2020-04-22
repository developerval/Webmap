import folium
import pandas

def colour_producer(elevation):
    if elevation <= 1500:
        return 'green'
    elif elevation >= 1501 and elevation <= 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location = [41.294, -116.323], zoom_start = 6, tiles = "Stamen Terrain")
data = pandas.read_csv('volcano.csv')
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")


coords = list(zip(list(data['LAT']), list(data['LON'])))
elevation = list(data['ELEV'])
volcano_name = list(data['NAME'])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %sm
"""


for latlon, elev, name in zip(coords, elevation, volcano_name):
    iframe = folium.IFrame(html=html % (name, name, elev), width=200, height=75)
    fgv.add_child(folium.CircleMarker(location=latlon, radius=6, popup=folium.Popup(iframe), fill_color=colour_producer(elev), color='grey', fill_opacity=0.6))

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("index.html")
