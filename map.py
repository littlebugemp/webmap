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

map = folium.Map(location=[29.48829406821279, 77.69980822497845],zoom_start=5)
fg = folium.FeatureGroup(name="My Map")

for lt,ln,n in zip(lat, lon, name):
    iframe = folium.IFrame(html=html % n, width = 200, height=100)
    fg.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color=color_producer(n))))
    #custom markers
    #fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=n,fill_color=color_producer(n),color='grey',fill_opacity=0.7))

map.add_child(fg)

map.save("Map1.html")