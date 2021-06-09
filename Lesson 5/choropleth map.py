import geopandas as gpd
from pyproj import CRS
import requests
import geojson
from pyproj import CRS
import folium

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
data = gpd.GeoDataFrame.from_features(geojson.loads(r.content))

data = data.set_crs(epsg=4326)
data = data.rename(columns={'asukkaita':'pop18'})
data['geoid'] = data.index.astype(str)

data = data[['geoid', 'pop18', 'geometry']]

m = folium.Map(location=[60.25, 24.8], tiles='cartodbpositron', zoom_start=10, control_scale=True)

folium.Choropleth(
    geo_data=data,
    name='Population in 2018',
    data=data,
    columns=['geoid', 'pop18'],
    key_on='feature.id',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    line_color='white', 
    line_weight=0,
    highlight=False, 
    smooth_factor=1.0,
    #threshold_scale=[100, 250, 500, 1000, 2000],
    legend_name= 'Population in Helsinki').add_to(m)

folium.features.GeoJson(data,  
                        name='Labels',
                        style_function=lambda x: {'color':'transparent','fillColor':'transparent','weight':0},
                        tooltip=folium.features.GeoJsonTooltip(fields=['pop18'],
                                                                aliases = ['Population'],
                                                                labels=True,
                                                                sticky=False
                                                                            )
                       ).add_to(m)

m

outfp = "choropleth_map.html"
m.save(outfp)