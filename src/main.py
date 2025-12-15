from fastapi import FastAPI, HTTPException
from models import TemperatureResponse
from weather_service import fetch_temperature

app = FastAPI()  # <- This is the ASGI app

@app.get("/temperature", response_model=TemperatureResponse)
def get_temperature(lat: float, lon: float):
    try:
        return fetch_temperature(lat, lon)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
