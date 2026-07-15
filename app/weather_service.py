import os
import requests
from fastapi import HTTPException

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"
GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"


def fetch_weather(location_query: str) -> dict:
    try:
        geo_resp = requests.get(
            GEO_URL,
            params={"q": location_query, "limit": 1, "appid": WEATHER_API_KEY},
            timeout=5,
        )
        geo_resp.raise_for_status()
        geo_data = geo_resp.json()

        if not geo_data:
            raise HTTPException(
                status_code=404,
                detail=f"Could not find a location matching '{location_query}'. "
                       f"Try a more specific name (e.g. include country or state)."
            )

        lat, lon = geo_data[0]["lat"], geo_data[0]["lon"]
        resolved_name = f"{geo_data[0].get('name')}, {geo_data[0].get('country', '')}".strip(", ")

        current_resp = requests.get(
            f"{BASE_URL}/weather",
            params={"lat": lat, "lon": lon, "appid": WEATHER_API_KEY, "units": "metric"},
            timeout=5,
        )
        current_resp.raise_for_status()

        forecast_resp = requests.get(
            f"{BASE_URL}/forecast",
            params={"lat": lat, "lon": lon, "appid": WEATHER_API_KEY, "units": "metric"},
            timeout=5,
        )
        forecast_resp.raise_for_status()

        return {
            "resolved_location": resolved_name,
            "current": current_resp.json(),
            "forecast": forecast_resp.json(),
        }

    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Weather service timed out. Please try again.")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Weather service is currently unavailable: {str(e)}")