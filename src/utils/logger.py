import logging
import os
from src.config import config

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(config.LOG_LEVEL)

    if not logger.handlers:
        # Resolve to project root correctly
        log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        import sys
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
        if hasattr(sys.stderr, 'reconfigure'):
            sys.stderr.reconfigure(encoding='utf-8')
        c_handler = logging.StreamHandler(sys.stdout)
        f_handler = logging.FileHandler(os.path.join(log_dir, "app.log"), encoding='utf-8')
        
        c_handler.setLevel(config.LOG_LEVEL)
        f_handler.setLevel(config.LOG_LEVEL)

        format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(format_str)

        c_handler.setFormatter(formatter)
        f_handler.setFormatter(formatter)

        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

    return logger
