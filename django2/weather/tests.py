import requests

response = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": 37.98,
        "longitude": -1.13,
        "current_weather": True,
        "wind_speed_unit": "kmh"
    }
)
response_json = response.json()
print(response_json)
print("Temperatura actual:", response_json['current_weather']['temperature'], "°C")