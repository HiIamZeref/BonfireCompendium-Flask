from app.config.dev_config import DevConfig
from app.config.production import ProductionConfig

class Config:
    def __init__(self) -> None:
        self.dev_config = DevConfig()
        self.production_config = ProductionConfig()