import os
import sys
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.DATA_SOURCE = os.getenv("DATA_SOURCE", "data/sample_alerts.csv")
        self.TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
        self.TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
        
        self.validate()

    def validate(self):
        if not self.DATA_SOURCE:
            print("ERROR: DATA_SOURCE no configurado.")
            sys.exit(1)

config = Config()
