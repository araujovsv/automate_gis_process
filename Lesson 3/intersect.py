from shapely.geometry import Point, Polygon, LineString, MultiLineString
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely import speedups
speedups.enabled

p1 = Point(24.952242, 60.1696017)
p2 = Point(24.976567, 60.1612500)

coords = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(coords)

# print(p1.within(poly))
# print(p2.within(poly))

# print(poly.contains(p1))

line_a = LineString([(0, 0), (1, 1)])
line_b = LineString([(1, 1), (0, 2)])

# print(line_a.intersects(line_b))
# print(line_a.touches(line_b))

# multi = MultiLineString([line_a, line_b])
# p = gpd.GeoSeries(multi)
# p.plot()
# plt.show()

fp = r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 3\join.shp'

data = gpd.read_file(fp)
#print(data.head())

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw' #ler KML com geopandas

fd = r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\site\data\PKS_suuralue.kml'
polys = gpd.read_file(fd, driver='KML')

southern = polys.loc[polys['Name'] == 'Eteläinen']
southern.reset_index(drop=True, inplace=True)
#print(southern.head())


# # Create a figure with one subplot
# fig, ax = plt.subplots()

# # Plot polygons
# polys.plot(ax=ax, facecolor='gray')
# southern.plot(ax=ax, facecolor='red')

# # Plot points
# data.plot(ax=ax, color='blue', markersize=5)

# plt.tight_layout()
# plt.show()

pip_mask = data.within(southern.at[0, 'geometry'])
#print(pip_mask)

pip_data= data.loc[pip_mask]
print(pip_data)

# Create a figure with one subplot
fig, ax = plt.subplots()

# Plot polygons
polys.plot(ax=ax, facecolor='gray')
southern.plot(ax=ax, facecolor='red')

# Plot points
pip_data.plot(ax=ax, color='gold', markersize=2)

plt.tight_layout()
plt.show()