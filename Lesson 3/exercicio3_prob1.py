import csv
import pandas as pd
import geopandas as gpd
from geopandas.tools import geocode
from pyproj import CRS
import requests
import geojson
import matplotlib.pyplot as plt

# with open('shopping_lists.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['id', 'name', 'addr'])
#     writer.writerow(['1', 'Park Shopping', 'SAI/SO Área 6580, s/n - Guará, Brasília - DF, 71219-900'])
#     writer.writerow(['2', 'Iguatemi Brasilia', 'St. de Habitações Individuais Norte CA 4 - Lago Norte, Brasília - DF, 71503-504'])
#     writer.writerow(['3', 'Conjunto Nacional', 'SDN, CNB - Asa Norte, Brasília - Distrito Federal, 70077-900'])
#     writer.writerow(['4', 'Patio Brasil', 'St. Comercial Sul - Asa Sul, Brasília - Distrito Federal, 70307-902'])
#     writer.writerow(['5', 'Boulevard Shopping', 'Setor Terminal Norte, Conj J - Asa Norte, Brasília - DF, 70770-100'])

df = pd.read_csv(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\site\data\addresses.txt', sep=';', header=0)
geo = geocode(df['addr'], provider='nominatim', user_agent='autogis_xx', timeout=4)

join = geo.join(df)
join['buffer'] = join.geometry.buffer(1500)
join = join.to_crs(epsg=3879)

# Specify the url for web feature service
url = 'https://kartta.hsy.fi/geoserver/wfs'

# Specify parameters (read data in json format).
# Available feature types in this particular data source: http://geo.stat.fi/geoserver/vaestoruutu/wfs?service=wfs&version=2.0.0&request=describeFeatureType
params = dict(service='WFS',
              version='2.0.0',
              request='GetFeature',
              typeName='asuminen_ja_maankaytto:Vaestotietoruudukko_2018',
              outputFormat='json')

# Fetch data from WFS using requests
r = requests.get(url, params=params)

# Create GeoDataFrame from geojson
pop = gpd.GeoDataFrame.from_features(geojson.loads(r.content))

pop = pop.rename(columns={'asukkaita': 'pop18'})
pop = pop[['pop18', 'geometry']]

pop.crs = CRS.from_epsg(3879).to_wkt()

join = join[['id', 'buffer']]
pop = pop.join(join)

grouped_pop = pop.groupby(by='id', as_index=False).sum()
print(grouped_pop)