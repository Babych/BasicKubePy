from fastapi import FastAPI, HTTPException
from models import TemperatureResponse
from weather_service import fetch_temperature

app = FastAPI()

@app.get("/temperature", response_model=float)
def get_temperature(lat: float, lon: float):
    try:
        response:TemperatureResponse = fetch_temperature(lat, lon)
        return response.temperature
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
