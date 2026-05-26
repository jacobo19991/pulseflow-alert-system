import requests
from src.config import config
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def send_alert(message: str) -> bool:
    token = config.TELEGRAM_BOT_TOKEN
    chat_id = config.TELEGRAM_CHAT_ID
    
    if not token or not chat_id or token == "your_telegram_bot_token_here":
        logger.warning("Credenciales de Telegram no configuradas. Simulando envío.")
        logger.info(f"[SIMULADO]\n{message}")
        return True
        
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        logger.error(f"Error enviando mensaje a Telegram: {str(e)}")
        return False
