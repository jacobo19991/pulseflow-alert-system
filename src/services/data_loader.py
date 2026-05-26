import pandas as pd
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def load_data(data_source: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(data_source)
        
        required_columns = {'id', 'title', 'description', 'status', 'priority', 'date'}
        if not required_columns.issubset(df.columns):
            missing = required_columns - set(df.columns)
            logger.error(f"Faltan columnas requeridas en el CSV: {missing}")
            return pd.DataFrame()
            
        logger.info(f"Cargadas {len(df)} alertas desde {data_source}")
        return df
    except FileNotFoundError:
        logger.error(f"Archivo no encontrado: {data_source}")
        return pd.DataFrame()
    except Exception as e:
        logger.error(f"Error al cargar los datos: {str(e)}")
        return pd.DataFrame()
