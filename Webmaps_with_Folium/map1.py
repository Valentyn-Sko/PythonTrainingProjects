import folium
import pandas


def color_p(elev):
    if elev < 1500:
        color_t = 'green'
    elif elev < 2000:
        color_t = 'orange'
    elif elev < 2500:
        color_t = 'red'
    else:
        color_t = 'black'
    return color_t


map = folium.Map(location=[50.45466, 30.4238], tiles="Stamen Terrain", zoom_start=8)
fg = folium.FeatureGroup(name="Volcanoes")

fg.add_child(folium.Marker(location=[50.4019288, 30.3874635], popup='Parking', icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[51.4019288, 30.3874635], popup='Parking', icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[52.4019288, 30.3874635], popup='Parking', icon=folium.Icon(color='green')))

for coordinates in [[50.4019288, 30.3], [50.4019288, 30.5]]:
    fg.add_child(folium.Marker(location=coordinates, popup='Parking', icon=folium.Icon(color='green', icon='ii')))

data = pandas.read_csv("points.txt")
list_n = list(data['NAME'])
list_lon = list(data['LON'])
list_lat = list(data['LAT'])
list_elev = list(data['ELEV'])

for name_p, lat_p, lon_p, el_p in zip(list_n, list_lon, list_lat, list_elev):
    fg.add_child(folium.CircleMarker(location=[lon_p, lat_p], popup=name_p, radius=7,
                                     fill_color=color_p(el_p), color='grey', fill_capacity=0.9))

fg1 = folium.FeatureGroup(name="Population")
fg1.add_child(folium.GeoJson(data=open('country_data.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000
                            else 'orange' if x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fg)
map.add_child(fg1)
map.add_child(folium.LayerControl())
map.save('Map1.html')
