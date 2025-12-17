import logging
import os
from datetime import datetime

from config import LOGS_DIR, NUM_LOGS


# CONFIGURACIÓN DE RUTAS ÚNICAS 
os.makedirs(LOGS_DIR, exist_ok=True) 

logs = sorted(
    [f for f in os.listdir(LOGS_DIR) if f.endswith(".log")],
    key=lambda x: os.path.getmtime(os.path.join(LOGS_DIR, x))
)

while len(logs) >= NUM_LOGS:
    oldest_log = logs.pop(0)
    os.remove(os.path.join(LOGS_DIR, oldest_log))


timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILENAME = f"simulacion_{timestamp}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILENAME)


# CONFIGURACIÓN DEL LOGGER 
logger = logging.getLogger("app_logger")  
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if logger.hasHandlers():
    logger.handlers.clear()

# Handler para consola
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Handler para archivo
file_handler = logging.FileHandler(LOG_FILE_PATH) 
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
