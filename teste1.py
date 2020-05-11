import pandas as pd
import geopandas
import matplotlib.pyplot as plt




df = pd.DataFrame(
    {'Coordinates': ['LINESTRING (30 10, 10 30, 40 40)', 'LINESTRING (32 10, 10 30, 40 40)',
                     'LINESTRING (33 10, 10 30, 40 40)', 'LINESTRING (34 10, 10 30, 40 40)',
                     'LINESTRING (35 10, 10 30, 40 40)']})
					 
#df = pd.read_csv('wkt.txt', header = None)

from shapely import wkt

df['Coordinates'] = df['Coordinates'].apply(wkt.loads)

gdf = geopandas.GeoDataFrame(df, geometry='Coordinates')

#print(gdf.head())

ax = world[world.continent == 'South America'].plot(color='white', edgecolor='black')

gdf.plot(ax=ax, color='red')

plt.show()
