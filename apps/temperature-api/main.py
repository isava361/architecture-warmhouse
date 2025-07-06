from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
import random
from datetime import datetime
import uvicorn

app = FastAPI(title="Temperature API", version="1.0.0")

class TemperatureResponse(BaseModel):
    value: float
    unit: str = "°C"
    timestamp: datetime
    location: str
    status: str = "ok"
    sensor_id: str
    sensor_type: str = "Thermometer"
    description: str

# Static mappings between locations and sensor IDs
LOCATION_TO_SENSOR = {
    "Living Room": "1",
    "Bedroom": "2",
    "Kitchen": "3",
}

SENSOR_TO_LOCATION = {v: k for k, v in LOCATION_TO_SENSOR.items()}

def resolve_location_sensor(location: str | None, sensor_id: str | None):
    """Fill in the missing piece between location and sensor_id based on fixed mapping."""
    # If no location provided, infer from sensor ID
    if not location:
        location = SENSOR_TO_LOCATION.get(sensor_id, "Unknown")

    # If no sensor_id provided, infer from location
    if not sensor_id:
        sensor_id = LOCATION_TO_SENSOR.get(location, "0")

    return location, sensor_id


@app.get("/temperature", response_model=TemperatureResponse)
async def get_temperature(
    location: str | None = Query(None, description="Room name"),
    sensor_id: str | None = Query(None, alias="sensorId", description="Sensor identifier"),
):
    """Return a simulated temperature reading for a room or sensor."""
    location, sensor_id = resolve_location_sensor(location, sensor_id)

    # Simulate a realistic indoor temperature in Celsius
    value = round(random.uniform(18.0, 28.0), 1)

    return TemperatureResponse(
        value=value,
        timestamp=datetime.utcnow(),
        location=location,
        sensor_id=sensor_id,
        description=f"Simulated temperature for {location}",
    )


@app.get("/temperature/{sensor_id}", response_model=TemperatureResponse)
async def get_temperature_by_id(sensor_id: str):
    """Return a simulated temperature reading for a given sensor ID."""
    location, sensor_id = resolve_location_sensor(None, sensor_id)

    # Simulate a realistic indoor temperature in Celsius
    value = round(random.uniform(18.0, 28.0), 1)

    return TemperatureResponse(
        value=value,
        timestamp=datetime.utcnow(),
        location=location,
        sensor_id=sensor_id,
        description=f"Simulated temperature for {location}",
    )


if __name__ == "__main__":
    # Run the API on port 8081 by default
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=False)
