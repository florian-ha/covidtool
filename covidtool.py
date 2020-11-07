import json, requests

apiurl = 'https://opendata.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0.geojson'

data = requests.get(apiurl).json()