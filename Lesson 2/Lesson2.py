import geopandas as gpd
import os
import matplotlib.pyplot as plt

# Trabalhar com shapefiles em locais distintos
input_folder = r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\L2_data\NLS\2018\L4\L41\L4132R.shp'

fp = os.path.join(input_folder, 'm_L4132R_p.shp')

data = gpd.read_file(fp)

#print(type(data)) #Geodataframe = é como uma tabela do pandas, com dados de vetor

print(data.columns)

data = data[['RYHMA', 'LUOKKA', 'geometry']]

colnames = {'RYHMA':'GROUP', 'LUOKKA':'CLASS'}

data.rename(columns = colnames, inplace=True)

print(data.shape)

# Fazendo o primeiro mapa, simples

#data.plot()
# plt.show()

#Geometrias

print(data['geometry'].head())

#Area do Polígono
#print("Polygon:", data.at[0, 'geometry'])
#print('Area:', round(data.at[0, 'geometry'].area,0), 'square meters')
#print(data['area'].max())

# for index, row in data[0:5].iterrows():
    # poly_area = row['geometry'].area
    # print('Polygon area at {index} is: {area:.2f} m^2'.format(index=index, area = poly_area))


# Clipando o shapefile

selection = data.loc[data["CLASS"] == 36200]

selection.plot()
plt.show()

output_folder = r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\L2_data\NLS\2018\L4'
output_fd = os.path.join(output_folder, 'Class_36200.shp')

# selection.to_fle(output_fd)


# Groupby e Exportando múltiplos shapefiles
grouped = data.groupby('CLASS')


# for key, group in grouped:
#     output_name = 'terrain_{}.shp'.format(key)
#     print("Saving file", output_name)
#     outpath = os.path.join(output_folder, output_name)
#     group.to_file(outpath)