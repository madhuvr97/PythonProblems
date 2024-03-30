import logging

def test_loggingDemo():
    # Get logger for the current module
    logger = logging.getLogger(__name__)

    # Create a file handler to write log messages to a file named 'logfile.log'
    fileHandler = logging.FileHandler('logfile.log')

    # Define a formatter to specify the format of log messages
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    # Set the formatter for the file handler
    fileHandler.setFormatter(formatter)

    # Add the file handler to the logger to handle logging to the file
    logger.addHandler(fileHandler)

    # Set the logging level for the logger.
    # In this case, all messages at or above the CRITICAL level will be logged.
    logger.setLevel(logging.CRITICAL)

    # Log messages at different levels for demonstration
    logger.debug("A debug statement is executed")  # This won't be logged because DEBUG < CRITICAL
    logger.info("Information statement")          # This won't be logged because INFO < CRITICAL
    logger.warning("Something is in warning mode") # This won't be logged because WARNING < CRITICAL
    logger.error("A Major error has happened")     # This will be logged because ERROR >= CRITICAL
    logger.critical("Critical issue")              # This will be logged because CRITICAL == CRITICAL

if __name__ == "__main__":
    test_loggingDemo()
