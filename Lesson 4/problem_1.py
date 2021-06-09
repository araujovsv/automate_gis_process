import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import mapclassify
import matplotlib.pyplot as plt

data1 = pd.read_csv(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\TravelTimes_to_5944003_Itis.txt', sep=';')
data2 = pd.read_csv(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\TravelTimes_to_5902043_Myyrmanni.txt', sep=';')


travel_time_itis = gpd.GeoDataFrame(data1)
travel_time_my = gpd.GeoDataFrame(data2)

travel_time_itis = travel_time_itis.loc[travel_time_itis['pt_r_t'] >= 0]
travel_time_itis = travel_time_itis.loc[travel_time_itis['car_r_t'] >= 0]
travel_time_itis = travel_time_itis[['pt_r_t', 'car_r_t', 'from_id', 'to_id']]

travel_time_my = travel_time_my.loc[travel_time_my['pt_r_t'] >= 0]
travel_time_my = travel_time_my.loc[travel_time_my['car_r_t'] >= 0]
travel_time_my = travel_time_my[['pt_r_t', 'car_r_t', 'from_id', 'to_id']]


grid1 = gpd.read_file(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\MetropAccess_YKR_grid_EurefFIN.shp')
data_geo_itis = grid1.merge(travel_time_itis, left_on='YKR_ID', right_on='from_id')
UserDefined_itis_pt = mapclassify.UserDefined(y=data_geo_itis['pt_r_t'], bins=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
UserDefined_itis_car = mapclassify.UserDefined(y=data_geo_itis['car_r_t'], bins=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])


grid2 = gpd.read_file(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\MetropAccess_YKR_grid_EurefFIN.shp')
data_geo_my = grid2.merge(travel_time_my, left_on='YKR_ID', right_on='from_id')
UserDefined_my_pt = mapclassify.UserDefined(y=data_geo_my['pt_r_t'], bins=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
UserDefined_my_car = mapclassify.UserDefined(y=data_geo_my['car_r_t'], bins=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

UserDefined_my_pts = mapclassify.UserDefined.make(bins=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

data_geo_my['nb_pt_r_t'] = data_geo_my[['pt_r_t']].apply(UserDefined_my_pts)
data_geo_my['nb_car_r_t'] = data_geo_my[['car_r_t']].apply(UserDefined_my_pts)
data_geo_my1 = data_geo_my

print(data_geo_my)
print(data_geo_my.columns)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
ax1= data_geo_my.plot(ax=ax1, column='nb_pt_r_t', linewidth=0)
ax2= data_geo_my.plot(ax=ax2, column='nb_car_r_t', linewidth=0)

fig.tight_layout()
plt.show()

