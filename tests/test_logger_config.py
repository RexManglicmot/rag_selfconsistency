import os
import time
from app.logger_config import logger

def test_logger_writes_to_log_file() -> None:   # It returns None, the test function returns nothing, as expected for test cases
    """
    Function that test that the logger from logger_config.py:
    1) Creates the log file at the expected location
    2) Writes log messages to that file correctly
    """

    log_path: str = os.path.join(os.getcwd(), "logs", "app.log")

    # Step 1: Check if the log file exists
    assert os.path.exists(log_path), "Log file does not exist"

    # Step 2: Write a unique test message to the logger
    test_message: str = f"TEST_LOG_{int(time.time())}"
    logger.info(test_message)

    # Step 3: Confirm the test message is in the log file
    with open(log_path, "r") as f:
        logs: str = f.read()
        assert test_message in logs, "Log message was not found in the log file"

# COMPLETE

