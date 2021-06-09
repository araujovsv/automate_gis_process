from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points
import geopandas as gpd
import pandas as pd

fp1 = r"C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\site\data\PKS_suuralue.kml"
fp2 = r"C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\site\data\addresses.shp"
orig = Point(1,1.67)
dest1 = Point(0, 1.45)
dest2 =Point(2, 2)
dest3 = Point(0, 2.5)

destinations = MultiPoint([dest1, dest2, dest3])
nearest_geoms = nearest_points(orig, destinations)
# print(nearest_geoms[0]) #o nosso ponto
# print(nearest_geoms[1]) #o ponto mais próximo

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

df1 = gpd.read_file(fp1, driver='KML')
df2 = gpd.read_file(fp2)

df1['centroid'] = df1.centroid

def get_nearest_values(row, other_gdf, point_column='geometry', value_column="geometry"):
    """Find the nearest point and return the corresponding value from specified value column."""
    
    # Create an union of the other GeoDataFrame's geometries:
    other_points = other_gdf["geometry"].unary_union
    
    # Find the nearest points
    nearest_geoms = nearest_points(row[point_column], other_points)
    
    # Get corresponding values from the other df
    nearest_data = other_gdf.loc[other_gdf["geometry"] == nearest_geoms[1]]
    
    nearest_value = nearest_data[value_column].values[0]
    
    return nearest_value

df1["nearest_loc"] = df1.apply(get_nearest_values, other_gdf=df2, point_column="centroid", value_column="id", axis=1)
print(df1)