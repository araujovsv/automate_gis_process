
import geopandas as gpd
from pyproj import CRS
import requests
import geojson
import matplotlib.pyplot as plt

addr_fp= r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\site\data\addresses.shp'
addresses = gpd.read_file(addr_fp)
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
addresses = addresses.to_crs(pop.crs)

join = gpd.sjoin(addresses,pop, how='inner', op='within')
print(join.head())
# # Create a figure with one subplot
# fig, ax = plt.subplots(figsize=(15,8))

# # Plot population grid
# pop.plot(ax=ax)

# # Plot points
# addresses.plot(ax=ax, color='red', markersize=5)

# fig, ax = plt.subplots(figsize=(10,6))
# join.plot(ax=ax, column='pop18', cmap='Reds', markersize=15, scheme='quantiles', legend=True)
# Create a figure with one subplot
fig, ax = plt.subplots(figsize=(10,6))

# Plot the grid with population info
pop.plot(ax=ax, column='pop18', cmap="Reds", scheme='quantiles', legend=True);

# Add title
plt.title("Population 2018 in 250 x 250 m grid squares");

# Remove white space around the figure
plt.tight_layout()
plt.show()