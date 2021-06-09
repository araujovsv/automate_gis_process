
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

grid = gpd.read_file(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 5\Data folder\TravelTimes_to_5975375_RailwayStation.shp')

data = grid.to_crs(epsg=3857)

#não é para adicionar o subplot, só pra controlar o tamanho da fig
fig, ax = plt.subplots(figsize=(12,8))

data.plot(ax=ax, column='pt_r_t', cmap='RdYlBu', linewidth=0, scheme='quantiles', k=9, alpha=0.0)
c