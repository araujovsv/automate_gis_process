import geopandas as gpd
from shapely.geometry import Point, Polygon
from pyproj import CRS

newdata = gpd.GeoDataFrame()

coordinates = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]

poly = Polygon(coordinates)

print(poly)

newdata.at[0, 'geometry'] = poly
newdata.at[0, 'location'] = 'Senaatintori'
newdata.crs = CRS.from_epsg(4326).to_wkt()

print(newdata)

newdata.crs = CRS.from_epsg(3067).to_wkt()
newdata.to_file(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\L2_data\Europe_borders_epsg3035.shp')
