import folium
import pandas
data = pandas.read_csv("valconoes.txt")
lat = list(data["LAT"])     #latitude
lon = list(data["LON"])     #longitude
elev = list(data["ELEV"])   #elevation

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <=elevation <= 2500:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.09],zoom_start=6,titles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius = 6 ,popup=str(el)+" m",fill_color = color_producer(el),color = 'grey',fill_opacity=0.7))
map.add_child(fg)

map.save("Map1.html")
