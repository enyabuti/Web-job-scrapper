import logging

logging.basicConfig(filename='logs/pipeline.log', level=logging.INFO)
def log(message):
    logging.info(message)