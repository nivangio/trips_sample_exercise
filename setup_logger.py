##This function creates different types of logger objects that will be then used to write logs

import logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
from logging.handlers import TimedRotatingFileHandler

def setup_logger(name, log_file, recurrency = None, formatter = formatter):
    """Function setup as many loggers as you want"""

    if recurrency is not None:
        handler = TimedRotatingFileHandler(log_file, when=recurrency, interval=1)
        handler.suffix = "%Y_%m_%d-%H.log"
    else:
        handler = logging.FileHandler(log_file)

    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger