import logging
import sys
from pythonjsonlogger import jsonlogger


def setup_logging() -> None:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )
    handler.setFormatter(formatter)

    # Replace default handlers to avoid duplicate logs
    logger.handlers = [handler]
