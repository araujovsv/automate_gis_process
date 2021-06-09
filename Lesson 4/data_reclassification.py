import geopandas as gpd
import matplotlib.pyplot as plt
import mapclassify

geoj = r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\site\data\TravelTimes_to_5975375_RailwayStation_Helsinki.geojson'
shpfile = r'C:\Users\victo\Desktop\Workstation 21\Pessoal\Code\VSCode\Automating GIS Process\site\data\TravelTimes_to_5975375_RailwayStation.shp'

acc = gpd.read_file(geoj)

#Excluindo os campos que não tem dados
acc = acc.loc[acc['pt_r_tt'] >= 0]

#Classificando os dados, como aqueles algoritmos no ArcGIS
classifier = mapclassify.NaturalBreaks(y=acc['pt_r_tt'], k=9)


#Criando um critério de classificação
classifier = mapclassify.NaturalBreaks.make(k=9)

#Classificando os dados, e gerando um dtaframe onde cada dado foi colocado em uma classe
classifications = acc[['pt_r_tt']].apply(classifier)

#adicionando a classificação no DF
acc['nb_pt_r_tt'] = acc[['pt_r_tt']].apply(classifier)

acc['nb_pt_r_tt'].plot.hist(bins=10)

classificator = mapclassify.NaturalBreaks(y=acc['pt_r_tt'], k=9)

for value in classificator.bins:
    plt.axvline(value, color='k', linestyle='dashed', linewidth=1)
plt.show()