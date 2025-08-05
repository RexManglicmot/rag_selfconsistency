# Import
import os
import logging
from logging.handlers import RotatingFileHandler

## Create a Log Directory

# Get absolute paths to the "logs" directory at the roof of the project.
# Remember it needs to set up first.
log_dir = os.path.join(os.getcwd(), "logs")

# Create the directory if it does not exist
os.makedirs(log_dir, exist_ok=True)

# Set the log file path
log_file = os.path.join(log_dir, "app.log")

## Configure Logger

# Create a named logger and this is the same name in all files that will import it
logger = logging.getLogger("subjectline")

# Set the min severity level: INFO, WARNING, ERROR, DEBUG, etc.
logger.setLevel(logging.INFO)

# Prevent duplicate handlers if this module is imported multiple times
if not logger.handlers:
    
    # Create a rotating file handler to keep logs manageable
    # maxBytes = 2MB per log file; backupCount = keep 3 old log files
    handler = RotatingFileHandler(
        log_file, maxBytes=2_000_000, backupCount=3
    )

    # Set a clear log format with timestamp, level, and message
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    handler.setFormatter(formatter)

    # Attach the handler to the logger
    logger.addHandler(handler)

# COMPLETE

