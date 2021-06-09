import csv
import pandas as pd
import geopandas as gpd
from geopandas.tools import geocode
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 3\shopping_lista.csv', sep=';', header=0)
geo = geocode(df['addr'], provider='nominatim', user_agent='autogis_xx', timeout=4)

join = geo.join(df)

join.to_file(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 3\join_ex3.shp')
join = join.to_crs(epsg=31983)

join['buffer'] = join.geometry.buffer(1500)
join['buffer'].plot()
join.plot()
plt.show()