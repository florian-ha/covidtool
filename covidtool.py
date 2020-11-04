import json, requests

apiurl = 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_COVID19/FeatureServer/0/query?where=1%3D1&outFields=Bundesland,Landkreis,AnzahlTodesfall,Meldedatum,Datenstand,AnzahlFall&outSR=4326&f=json'

data = requests.get(apiurl).json()