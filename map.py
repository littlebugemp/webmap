import folium
import pandas

vol_details = pandas.read_csv('val_in_india.csv')
#print(vol_details.columns)
lat = vol_details.LAT
lon = vol_details.LON
name= vol_details.Name

def color_producer(element):
    if 'a' in element:
        return 'red'
    else:
        return 'blue'

html = """<h4>Volcano Information:</h4>
Name : %s
"""
#creating map object
map = folium.Map(location=[29.48829406821279, 77.69980822497845],zoom_start=5)
#adding feature group
fgp = folium.FeatureGroup(name="population")
fgv = folium.FeatureGroup(name="volcanos")

for lt,ln,n in zip(lat, lon, name):
    iframe = folium.IFrame(html=html % n, width = 200, height=100)
    #fg.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color=color_producer(n))))
    #custom markers
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=n,fill_color=color_producer(n),color='grey',fill_opacity=0.7))

#adding polygon using json GeoJson
fgp.add_child(folium.GeoJson(data=(open("world.json",'r',encoding='utf-8-sig').read()),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

#adding feature group to map
map.add_child(fgv)
map.add_child(fgp)
#adding Layer Controler
map.add_child(folium.LayerControl())
#saving map into html
map.save("Map1.html")
