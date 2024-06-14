# %%
from geoclip import GeoCLIP
import folium

model = GeoCLIP()
image_path = input("Image to predict location")

top_pred_gps, top_pred_prob = model.predict(image_path, top_k=10)

coordinates = [{'name': f'Point {idx}', 'lat': lat, 'lon': lon } for idx, (lat, lon) in enumerate(top_pred_gps)]

# Create a map centered around the first point
m = folium.Map(location=[coordinates[0]['lat'], coordinates[0]['lon']], zoom_start=5)

# Add points to the map
for point in coordinates:
    folium.Marker(
        location=[point['lat'], point['lon']],
        popup=point['name']
    ).add_to(m)

m
