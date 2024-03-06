
"""
Log Handlers

This module contains utility functions to set up logging
consistently
"""
import logging


def init_logging(app, logger_name: str):
    """Set up logging for production"""
    app.logger.propagate = False
    gunicorn_logger = logging.getLogger(logger_name)
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    # Make all log formats consistent
    format_string = "[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s"
    formatter = logging.Formatter(format_string, "%Y-%m-%d %H:%M:%S %z")
    for handler in app.logger.handlers:
        handler.setFormatter(formatter)
    app.logger.info("Logging handler established")
