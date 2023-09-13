import logging
import os
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_directory = "logs"

# Create the "logs" directory if it doesn't exist
os.makedirs(logs_directory, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILE_NAME)

# Create a custom file handler with flush=True to disable buffering
file_handler = logging.FileHandler(LOG_FILE_PATH, mode='a')
file_handler.setLevel(logging.INFO)

# Define log format
formatter = logging.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Create and configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)

# Now you can use the logger to log messages
logger.info("This is an example log message.")

# Close the file handler when you're done with logging
file_handler.close()


