import json, requests, folium

print("Loading data...")
apiurl = 'https://opendata.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0.geojson'
data = requests.get(apiurl).json()
print("Data loaded!")

m = folium.Map(location=[51.629,10.867], zoom_start=6)
folium.GeoJson(data).add_to(m)
print("Saving data...")
m.save("index.html")
print("Saved data to index.html")
