import requests
import time
import random

SERVER_URL = "http://localhost:5000/update-location"  # Flask server URL

# Starting location (bus starting point)
lat = 11.312093 
lng = 77.676380

while True:
    # Randomly move bus
    lat += random.uniform(-0.0003, 0.0003)
    lng += random.uniform(-0.0003, 0.0003)
    # Prepare POST data
    data = {
        "lat": lat,
        "lng": lng
    }

    try:
        r = requests.post(SERVER_URL, data=data)
        print(f"Sent: {lat:.6f}, {lng:.6f}, Response: {r.text}")
    except Exception as e:
        print("Error sending data:", e)

    time.sleep(3)  # 5 sec interval like ESP32
