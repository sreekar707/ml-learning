from logger import logging


def add(a,b):
    logging.debug("addition")
    
    return a+b

logging.debug("addition")
add(1,4)