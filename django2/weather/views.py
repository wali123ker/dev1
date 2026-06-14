import requests
from django.shortcuts import render

def weather_view(request):
    try:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": 37.98,
                "longitude": -1.13,
                "current_weather": True,
                "wind_speed_unit": "kmh",
                "forecast_days": 1
            },
            timeout=5
        )
        data = response.json()
        weather = data.get('current_weather', {})
    except Exception:
        weather = {}

    return render(request, 'weather/weather.html', {'weather': weather})