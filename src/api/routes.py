"""API routes for geolocation analysis"""
from fastapi import APIRouter, File, UploadFile
from src.services.geolocation import analyze_image

router = APIRouter()

@router.post("/analyze")
async def analyze_location(file: UploadFile = File(...)):
    """Analyze image and return geolocation data"""
    result = await analyze_image(file)
    return {"location": result}
# Modified 2025-08-15
# Modified 2025-07-20
# Modified 2022-07-31
# Modified 2024-04-01
# Modified 2024-04-22
