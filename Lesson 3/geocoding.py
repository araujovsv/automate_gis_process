import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from geopandas.tools import geocode

fp = r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\site\data\addresses.txt'

data = pd.read_csv(fp, sep=';')
geo = geocode(data['addr'], provider='nominatim', user_agent='autogis_xx', timeout=4)
print(geo.head())

join = geo.join(data)
print(join.head())

join.to_file(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 3\join.shp')