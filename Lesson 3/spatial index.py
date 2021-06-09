
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
# Filepaths
intersections_fp = r"C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\site\source\notebooks\L3\data\uusimaa_intersections.gpkg"
postcode_areas_fp = r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\site\source\notebooks\L3\data\uusimaa_postal_code_areas.gpkg'

intersections = gpd.read_file(intersections_fp)
postcode_areas = gpd.read_file(postcode_areas_fp)

# ax= postcode_areas.plot(color='red', edgecolor='black', alpha=0.5)
# ax = intersections.plot(ax=ax, color='yellow', markersize=1, alpha=0.5)
# ax.set_xlim([380000, 395000])
# ax.set_ylim([6667500, 6680000])
# plt.show()

intersection_sindex = intersections.sindex

city_center_zip_area = postcode_areas.loc[postcode_areas['posti_alue']=='00100']
# city_center_zip_area.plot()
# plt.show()

#JEITO DEMORADO
# Get the bounding box coordinates of the Polygon as a list
bounds = list(city_center_zip_area.bounds.values[0])
# Get the indices of the Points that are likely to be inside the bounding box of the given Polygon
point_candidates_idx = list(intersection_sindex.intersection(bounds))
point_candidates = intersections.loc[point_candidates_idx]

# ax = city_center_zip_area.plot(color='red', alpha=0.5)
# ax = point_candidates.plot(ax=ax, color='black', markersize=2)
# plt.show()

final_selection = point_candidates.loc[point_candidates.intersects(city_center_zip_area['geometry'].values[0])]
# ax = city_center_zip_area.plot(color='red', alpha=0.5)
# ax = final_selection.plot(ax=ax, color='black', markersize=2)
# plt.show()


def intersect_using_spatial_index(source_gdf, intersecting_gdf):
    """
    Conduct spatial intersection using spatial index for candidates GeoDataFrame to make queries faster.
    Note, with this function, you can have multiple Polygons in the 'intersecting_gdf' and it will return all the points
    intersect with ANY of those geometries.
    """
    source_sindex = source_gdf.sindex
    possible_matches_index = []

    # 'itertuples()' function is a faster version of 'iterrows()'
    for other in intersecting_gdf.itertuples():
        bounds = other.geometry.bounds
        c = list(source_sindex.intersection(bounds))
        possible_matches_index += c

    # Get unique candidates
    unique_candidate_matches = list(set(possible_matches_index))
    possible_matches = source_gdf.iloc[unique_candidate_matches]

    # Conduct the actual intersect
    result = possible_matches.loc[possible_matches.intersects(intersecting_gdf.unary_union)]
    return result

#Spatial Join
intersection_cnt = gpd.sjoin(postcode_areas, intersections).groupby('posti_alue').size().reset_index()

intersection_cnt = intersection_cnt.rename(columns={0:'intersection_cnt'})
postcode_areas = postcode_areas.merge(intersection_cnt, on='posti_alue')
print(postcode_areas)

#intersection density

m2_to_km2_converter = 1000000
postcode_areas['intersection_density'] = postcode_areas['intersection_cnt']/(postcode_areas.area/m2_to_km2_converter)
postcode_areas.plot('intersection_density', cmap='RdYlBu_r', legend=True)
plt.show()