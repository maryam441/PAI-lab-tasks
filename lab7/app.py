from flask import Flask, render_template
import requests

app = Flask(__name__)

NASA_API_KEY = "16OdOLAp67XlbxlY0TgtbZDorieiXRyXAf2pGWjI"
APOD_URL = "https://api.nasa.gov/planetary/apod"

@app.route("/", methods=["GET"])
def index():
    # Fetch APOD data from NASA API
    params = {"api_key": NASA_API_KEY}
    response = requests.get(APOD_URL, params=params)

    if response.status_code == 200:
        apod_data = response.json()
        
        # Debugging: Print API response
        print("API Response:", apod_data)  

        # Ensure HTTPS for the URL
        if "url" in apod_data and apod_data["url"].startswith("http://"):
            apod_data["url"] = apod_data["url"].replace("http://", "https://")

        return render_template("index.html", apod=apod_data, error=None)

    else:
        error_message = f"Error fetching data: {response.status_code} - {response.text}"
        print(error_message)  # Debugging
        return render_template("index.html", apod=None, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)  # Debug mode enabled for testing
