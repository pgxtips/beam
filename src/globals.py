from flask import Flask
from typing import Optional
from src.models.app_data import AppData

APP_SERVER: Optional[Flask] = None
APP_DATA: Optional[AppData] = None
