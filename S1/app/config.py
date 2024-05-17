from pydantic import BaseSettings

class Settings(BaseSettings):
    model_path: str = "yolov4.weights"

    class Config:
        env_file = ".env"
