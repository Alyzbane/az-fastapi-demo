import sys
from loguru import logger

logger.remove()  # Remove the default logger

logger.add(
    sys.stdout,
    level="DEBUG",
)

# Add file handler for persistent logging
logger.add(
    "logs/{time:YYYY-MM-DD}.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG",
    rotation="12:00",
    retention="7 days",
)
