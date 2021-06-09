import geopandas as gpd
from pyproj import CRS
import matplotlib.pyplot as plt

grid = gpd.read_file(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 5\Data folder\TravelTimes_to_5975375_RailwayStation.shp')
roads = gpd.read_file(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 5\Data folder\roads.shp')
metro = gpd.read_file(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 5\Data folder\metro.shp')

roads = roads.to_crs(crs=grid.crs)
metro = metro.to_crs(crs=grid.crs)

my_map = grid.plot(column='car_r_t', linewidth=0.03, cmap='Spectral', scheme='quantiles', k=9, alpha=0.9)

#definindo esse ax=my_map, eu tô projetando um em cima do outro
roads.plot(ax=my_map, color='grey', linewidth = 1.5)

#mais em cima ainda
metro.plot(ax=my_map, color='red', linewidth=2.5)

plt.tight_layout()

plt.savefig('static_map.png', dpi=300)
plt.show()