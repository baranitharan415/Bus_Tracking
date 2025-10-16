import requests
import time

# ✅ Start and End Coordinates
start = (11.3120932, 77.676380)
end = (11.0788254, 77.886791)

# ✅ Get route from OSRM (OpenStreetMap routing)
url = f"http://router.project-osrm.org/route/v1/driving/{start[1]},{start[0]};{end[1]},{end[0]}?overview=full&geometries=geojson"
response = requests.get(url)
route_data = response.json()

# ✅ Extract coordinates (lat, lon)
coords = route_data['routes'][0]['geometry']['coordinates']
path = [(lat, lon) for lon, lat in coords]

print(f"Total points in route: {len(path)}")
print("🚍 Starting bus simulation...\n")

# ✅ Flask server endpoint
# flask_url = "http://localhost:5000/update-location"
flask_url = "https://f2e4dd9527bb.ngrok-free.app/update-location"
# ✅ Simulate bus movement
for i, (lat, lon) in enumerate(path):
    try:
        # Send current location to Flask server
        data = {'lat': lat, 'lng': lon}
        res = requests.post(flask_url, data=data)

        if res.status_code == 200:
            print(f"✅ Step {i+1}/{len(path)}: Sent {lat:.6f}, {lon:.6f}")
        else:
            print(f"⚠️ Failed to send at step {i+1}")

        time.sleep(0.5)  # move every 0.5 sec (smooth)
    except Exception as e:
        print(f"❌ Error sending data: {e}")
        time.sleep(1)
