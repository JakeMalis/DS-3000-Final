import geopandas as gpd
from shapely.geometry import Point, box
import contextily as ctx

# Filter for cancelled departures
cancelled = flights_df[flights_df['CANCELLED'] == 1]

# Group by airport to count cancellations
agg = cancelled.groupby(['ORIGIN_AIRPORT', 'origin_airport/LATITUDE', 'origin_airport/LONGITUDE']) \
               .size() \
               .reset_index(name='cancellations')

# Create geometry from the longitude and latitude columns
agg['geometry'] = agg.apply(lambda row: Point(row['origin_airport/LONGITUDE'], row['origin_airport/LATITUDE']), axis=1)

# Convert to a GeoDataFrame
gdf = gpd.GeoDataFrame(agg, geometry='geometry')
gdf.set_crs(epsg=4326, inplace=True)

# Reproject to Web Mercator for contextily
gdf_3857 = gdf.to_crs(epsg=3857)

# Define the bounding box for the continental US in EPSG:4326
# Approximate coordinates: (-125, 24) to (-66, 50)
bbox = box(-125, 24, -66, 50)
bbox_gdf = gpd.GeoDataFrame({'geometry': [bbox]}, crs='epsg:4326')
bbox_3857 = bbox_gdf.to_crs(epsg=3857)

# Get the bounds (xmin, ymin, xmax, ymax)
xmin, ymin, xmax, ymax = bbox_3857.total_bounds

# Plot and add basemap with extent to focus on the continental US
fig, ax = plt.subplots(figsize=(12, 8))
gdf_3857.plot(ax=ax, markersize=gdf_3857['cancellations']*2, color='red', alpha=0.6, legend=True)
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_title("Cancellation Counts at Departure Airports within Continental US")
plt.show()