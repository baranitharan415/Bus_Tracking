from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_location = {"lat":0, "lng":0}

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/update-location', methods=['POST'])
def update_location():
    lat = float(request.form['lat'])
    lng = float(request.form['lng'])
    latest_location['lat'] = lat
    latest_location['lng'] = lng
    print(f"Received: {lat}, {lng}")
    return "OK"

@app.route('/location', methods=['GET'])
def get_location():
    return jsonify(latest_location)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
