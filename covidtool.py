import folium
import requests

# Loads Geojson from RKI Api
print("Loading data...")
apiurl = 'https://opendata.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0.geojson'
data = requests.get(apiurl).json()
print("Data loaded!")

# Creates and saves new Folium Map with counties in Germany
m = folium.Map(location=[51.629, 10.867], zoom_start=6)
folium.GeoJson(data).add_to(m)
print("Saving data...")
m.save("index.html")
print("Saved data to index.html")