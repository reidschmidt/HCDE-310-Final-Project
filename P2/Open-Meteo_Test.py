
import json
import ssl
import certifi
from urllib.request import urlopen
from urllib.parse import urlencode

# Seattle coordinates
params = {
    "latitude": 47.6062,
    "longitude": -122.3321,
    "current": "temperature_2m,precipitation,weather_code,is_day",
    "temperature_unit": "fahrenheit"
}

# Build the API request
url = "https://api.open-meteo.com/v1/forecast?" + urlencode(params)

# Use updated trusted certificates
context = ssl.create_default_context(cafile=certifi.where())

# Send request and read response
with urlopen(url, context=context, timeout=20) as response:
    data = json.loads(response.read().decode("utf-8"))

# Print current weather information
print(json.dumps(data["current"], indent=4))
