import geopandas as gpd
import matplotlib.pyplot as plt
# Load the shapefile
world = gpd.read_file(r"sample.shp")
print(world.head())
world.plot(column='POP_EST', cmap='viridis', legend=True, edgecolor='black')
plt.title('World Map - Population Visualization')
plt.show()
