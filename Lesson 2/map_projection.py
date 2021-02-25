import geopandas as gpd 
import matplotlib.pyplot as plt


fp = r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\L2_data\Europe_borders.shp'
data = gpd.read_file(fp)


# Reprojetando coordenadas
data_wgs84 = data.copy() #backup

data = data.to_crs(epsg=3035)

#Comparando
# fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 8))

# data_wgs84.plot(ax=ax1, facecolor = 'gray');

# ax1.set_title('WGS 84');

# data.plot(ax=ax2, facecolor ='blue');

# ax2.set_title('Lamber Azimuthal')

# plt.tight_layout()

# plt.show()

outfp = r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\L2_data\Europe_borders_epsg3035.shp'
data.to_file(outfp)

