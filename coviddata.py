#RKI Corona Landkreise: https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0

import pandas as pd
import requests
import openpyxl

print("Starting download of data...")
csvurl = 'https://opendata.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0.csv'
r = requests.get(csvurl)

with open('data.csv', 'wb') as f:
    f.write(r.content)
print("Finished downloading!")

df = pd.read_csv('data.csv')
df.to_excel(r'data.xlsx', index=False)
df.sort_values(by=['cases7_per_100k'],inplace=True ,ascending=False)
casesandnames = df[['GEN','BEZ','BL','cases7_per_100k']]
print(casesandnames)
casesandnames.to_excel(r'casesandnames.xlsx', index=False)