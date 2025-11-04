import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# This variable IS the final file path
LOG_FILE_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the directory from the path
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

# This line was the error and should be removed:
# LOG_FILE_PATH = os.path.join(log_path, LOG_FILE) 

logging.basicConfig(
    filename=LOG_FILE_PATH,  # Use the correct path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)