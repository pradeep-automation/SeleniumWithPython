import logging

import pytest


# @pytest.fixture(scope="session", autouse=True)
# def configure_logging():
#     # Configure logging with a level of INFO
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s [%(levelname)s] - %(message)s",
#         datefmt="%Y-%m-%d %H:%M:%S",
#     )

def test_example():
    # Log messages at various levels
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    # logging.getLogger().setLevel(logging.INFO)
    logging.debug("This is a debug message")     # Won't be captured
    logging.info("This is an info message")        # Will be captured
    logging.warning("This is a warning message")   # Will be captured
    logging.error("This is an error message")       # Will be captured
    logging.critical("This is a critical message") # Will be captured
