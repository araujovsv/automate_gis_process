import geopandas as gpd
from pyproj import CRS
from shapely.geometry import Point
import matplotlib.pyplot as plt

fp = r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\L2_data\Europe_borders_epsg3035.shp'

data = gpd.read_file(fp)


# Create the point representing Helsinki (in WGS84)
hki_lon = 24.9417
hki_lat = 60.1666

helsinki = gpd.GeoDataFrame([[Point(hki_lon, hki_lat)]], geometry= 'geometry', crs={'init': 'epsg:4326'}, columns=['geometry'])
print(helsinki)

aeqd = CRS(proj='aeqd', ellps='WGS84', datum='WGS84', lat_0=hki_lat, lon_0=hki_lon).srs

helsinki = helsinki.to_crs(crs=aeqd)

print(helsinki)

print('\nCRS:\n', helsinki.crs)

#Agora que Helsinki é o ponto 0, temos a distância de qualquer ponto até a cidade
europe_borders_aeqd = data.copy()

europe_borders_aeqd = europe_borders_aeqd.to_crs(crs=aeqd)

europe_borders_aeqd['centroid'] = europe_borders_aeqd.centroid
print(europe_borders_aeqd.head())

# Função para calcular distância

def calculate_distance(row, dest_geom, src_col='geometry', target_col='distance'):
    """
    Calculates the distance between Point geometries.

    Parameters
    ----------
    dest_geom : shapely.Point
       A single Shapely Point geometry to which the distances will be calculated to.
    src_col : str
       A name of the column that has the Shapely Point objects from where the distances will be calculated from.
    target_col : str
       A name of the target column where the result will be stored.

    Returns
    -------

    Distance in kilometers that will be stored in 'target_col'.
    """

    # Calculate the distances
    dist = row[src_col].distance(dest_geom)

    # Convert into kilometers
    dist_km = dist / 1000

    # Assign the distance to the original data
    row[target_col] = dist_km
    return row

helsinki_geom = helsinki.loc[0, 'geometry']

# Função Apply, que aplica a função em todas as colunas do seu dataframe
europe_borders_aeqd = europe_borders_aeqd.apply(calculate_distance, dest_geom=helsinki_geom, src_col='centroid', target_col='dist_to_Hki', axis=1)