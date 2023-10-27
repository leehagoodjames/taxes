# Standard Library imports
import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) # https://docs.python.org/3/library/logging.html#levels

# Create a stream handler that writes log messages to stdout
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter('[[%(asctime)s - %(levelname)s]] - %(message)s')
sh.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(sh)
sh = logging.StreamHandler(sys.stderr)
