import os
import json
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

PROCESSED_ALERTS_FILE = 'processed_alerts.json'

def load_processed_alerts() -> list:
    if os.path.exists(PROCESSED_ALERTS_FILE):
        try:
            with open(PROCESSED_ALERTS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error cargando alertas procesadas: {str(e)}")
            return []
    return []

def save_processed_alerts(processed_ids: list):
    try:
        with open(PROCESSED_ALERTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(processed_ids, f, indent=4)
    except Exception as e:
        logger.error(f"Error guardando alertas procesadas: {str(e)}")

def process_alerts(df) -> list:
    if df.empty:
        return []
        
    critical_alerts = df[df['status'].str.lower() == 'critical']
    processed_ids = load_processed_alerts()
    
    new_alerts = []
    for _, row in critical_alerts.iterrows():
        alert_id = str(row['id'])
        if alert_id not in processed_ids:
            new_alerts.append(row.to_dict())
            
    return new_alerts

def format_message(alert: dict) -> str:
    return (
        f"🚨 *ALERTA CRÍTICA* 🚨\n\n"
        f"🔹 *ID:* {alert.get('id')}\n"
        f"🔹 *Título:* {alert.get('title')}\n"
        f"🔹 *Fecha:* {alert.get('date')}\n"
        f"🔹 *Prioridad:* {alert.get('priority')}\n\n"
        f"📝 *Descripción:* {alert.get('description')}"
    )
