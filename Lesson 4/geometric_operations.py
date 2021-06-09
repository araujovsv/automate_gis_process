import geopandas as gpd
import matplotlib.pyplot as plt
import shapely.speedups

hel = gpd.read_file(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\site\data\Helsinki_borders.shp')
grid = gpd.read_file(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\site\data\TravelTimes_to_5975375_RailwayStation.shp')

# ax = grid.plot(facecolor='gray')
# hel.plot(ax=ax, facecolor='None', edgecolor='blue')
# plt.show()

assert hel.crs == grid.crs, 'CRS differs between layers!'

#Intersection entre ambos
intersection = gpd.overlay(grid, hel, how='intersection')
# intersection.plot()
# plt.show()

#Agregando dados por meio de uma coluna, no caso, o tempo de viagem
## Cada um dos tempos de viagem vira uma çinha, e ele agrega todas as geometrias que tem o mesmo valor de tempo de viagem
dissolved = intersection.dissolve(by='car_r_t')
print(dissolved)

selection = gpd.GeoDataFrame([dissolved.loc[15]], crs=dissolved.crs)
# ax = dissolved.plot(facecolor='gray')
# selection.plot(ax=ax, facecolor='red')
# plt.show()

