import logging


def setup_logger():
    logger = logging.getLogger("stock_bot")
    logger.setLevel(logging.DEBUG)

    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(ch)

    return logger
