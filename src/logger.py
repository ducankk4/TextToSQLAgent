import logging

def setup_logger():
    logging.basicConfig(
        level= logging.INFO,
        format= '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d - %(funcName)s()] - %(message)s',
        filename= 'app.log',
        filemode= 'w',
        encoding= 'utf-8'
    )
    logger = logging.getLogger()
    return logger

logger = setup_logger()
