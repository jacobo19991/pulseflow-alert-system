import time
from src.config import config
from src.utils.logger import setup_logger
from src.services.data_loader import load_data
from src.services.alert_processor import load_processed_alerts, save_processed_alerts, process_alerts, format_message
from src.services.notifier import send_alert

logger = setup_logger(__name__)

def main():
    logger.info("Iniciando PulseFlow...")
    
    df = load_data(config.DATA_SOURCE)
    
    if df.empty:
        logger.warning("No hay datos para procesar o hubo un error de carga.")
        return
        
    new_alerts = process_alerts(df)
    
    if not new_alerts:
        logger.info("No se encontraron nuevas alertas críticas.")
        return
        
    logger.info(f"Se procesarán {len(new_alerts)} alertas críticas.")
    
    processed_ids = load_processed_alerts()
    enviadas_correctamente = 0
    
    for alert in new_alerts:
        message = format_message(alert)
        if send_alert(message):
            processed_ids.append(str(alert['id']))
            enviadas_correctamente += 1
        time.sleep(1) # Rate limiting respect
            
    save_processed_alerts(processed_ids)
    logger.info(f"Resumen Final: {enviadas_correctamente}/{len(new_alerts)} alertas enviadas exitosamente.")

if __name__ == "__main__":
    main()
