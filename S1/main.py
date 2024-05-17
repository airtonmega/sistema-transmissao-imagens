from fastapi import FastAPI, UploadFile, File, HTTPException
import cv2
import numpy as np
from .config import Settings
from .services.detection_service import DetectionService
from .utils.image_utils import decode_image

app = FastAPI()
settings = Settings()
detection_service = DetectionService(settings.model_path)

@app.post("/detect/{client_id}")
async def detect(client_id: str, file: UploadFile = File(...)):
    try:
        image = decode_image(file.file.read())
        boxes, scores, class_ids = detection_service.detect(image, client_id)
        person_count = detection_service.count_people(class_ids)
        return {"person_count": person_count, "boxes": boxes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
