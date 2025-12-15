from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/temperature")
def get_temperature(lat: float, lon: float):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current=temperature_2m"
    )

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    data = response.json()
    return {
        "latitude": lat,
        "longitude": lon,
        "temperature": data["current"]["temperature_2m"],
        "unit": data["current_units"]["temperature_2m"]
    }
