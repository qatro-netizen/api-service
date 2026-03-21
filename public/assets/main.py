# main.py

import os
import logging
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a simple data model
class Device(BaseModel):
    id: int
    name: str
    description: str


# Create a FastAPI app
app = FastAPI()

# Define a route to return a list of devices
@app.get("/devices")
async def get_devices():
    # Simulate data from a database
    devices = [
        Device(id=1, name="Device 1", description="This is device 1"),
        Device(id=2, name="Device 2", description="This is device 2")
    ]
    return JSONResponse(content=[device.dict() for device in devices], media_type="application/json")

# Define a route to return a single device by ID
@app.get("/devices/{device_id}")
async def get_device(device_id: int):
    # Simulate data from a database
    devices = [
        Device(id=1, name="Device 1", description="This is device 1"),
        Device(id=2, name="Device 2", description="This is device 2")
    ]
    device = next((device for device in devices if device.id == device_id), None)
    if device:
        return JSONResponse(content=device.dict(), media_type="application/json")
    else:
        return JSONResponse(content={"error": "Device not found"}, status_code=404, media_type="application/json")

# Define a route to create a new device
@app.post("/devices")
async def create_device(device: Device):
    # Simulate creating a new device in a database
    device.id = len([d.id for d in [Device(id=1, name="Device 1", description="This is device 1"), Device(id=2, name="Device 2", description="This is device 2")]]) + 1
    return JSONResponse(content=device.dict(), media_type="application/json")

# Run the app
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)