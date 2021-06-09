import geopandas as gpd
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

metrop = gpd.read_file(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\MetropAccess_YKR_grid_EurefFIN.shp')


filepaths = []
path = os.listdir(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\Traveltime')
for file in path:
    path_for_arq = r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\Traveltime'
    final_path = path_for_arq + '\\' + file
    filepaths.append(final_path)

shop1 = pd.read_csv(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\Traveltime\TravelTimes_to_5878070_Jumbo.txt', sep=';')
shop2 = pd.read_csv(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\Traveltime\TravelTimes_to_5878087_Dixi.txt', sep=';')
shop3 = pd.read_csv(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\Traveltime\TravelTimes_to_5902043_Myyrmanni.txt', sep=';')
shop4 = pd.read_csv(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\Traveltime\TravelTimes_to_5944003_Itis.txt', sep=';')
shop5 = pd.read_csv(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\Traveltime\TravelTimes_to_5975373_Forum.txt', sep=';')
shop6 = pd.read_csv(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\Traveltime\TravelTimes_to_5978593_IsoOmena.txt', sep=';')
shop7 = pd.read_csv(r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\Lesson 4\data\Traveltime\TravelTimes_to_5980260_Ruoholahti.txt', sep=';')
shops = [shop2, shop3, shop4, shop5, shop6, shop7]

a = 1
for i in shops:
    a = a+1
    shop1['pt_r_t_{}'.format(a)] = i['pt_r_d']

shop = gpd.GeoDataFrame(shop1)
print(shop.columns)
metrop['pt_r_t'] = shop['pt_r_t']
for i in range(2,8):
    metrop['pt_r_t_{}'.format(i)] = shop['pt_r_t_{}'.format(i)]

metrops = metrop[['pt_r_t_2', 'pt_r_t_3', 'pt_r_t_4', 'pt_r_t_5', 'pt_r_t_6', 'pt_r_t_7']]
metrop['min_t'] = metrops.min(axis=1)
metrop['dominant_service'] = metrops.idxmin(axis='columns')
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
ax1 = metrop.plot(ax=ax1, column='dominant_service', legend=True)
ax2 = metrop.plot(ax=ax2, column='min_t', linewidth=0, legend=True)
# fig.tight_layout()
# plt.show()


