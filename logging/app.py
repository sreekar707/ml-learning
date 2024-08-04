import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log")
        
    ]
)
logger=logging.getLogger("ARITHMETIC APP")

def add (a,b):
    result=a+b
    logger.debug(f"the addition of numbers {a} + {b} = {result}")
    return result


def subtract(a,b):
    result=a-b
    logger.debug(f"the subtraction of numbers {a} - {b} = {result}")
    return result
     
def multiplication(a,b):
    result=a*b
    logger.debug(f"this is the multiplication of numbers {a} * {b} = {result}")
    return result


def division(a,b):
    try:
        result=a/b
        logger.debug(f"this is the division of numbers {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        
        
add(10,20) 
subtract(20,10)
multiplication(10,3)   
division(10,5)

