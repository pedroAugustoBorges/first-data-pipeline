import logging

def init_logger():
    
    root = logging.getLogger()
    
    if root.handlers:
        return
    
    logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s = %(message)s',
                        handlers= [logging.FileHandler('log.log'),
                                   logging.StreamHandler()])
    
    logging.info('Start of program and logger')
    


    
def init_logger_pro():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s = %(message)s')
    
    #console: INFO
    console_handler =  logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    #file: DEBUG
    debug_file_handler = logging.FileHandler('debug.log')
    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(formatter)
    
    #file:ERROR
    error_file_handler = logging.FileHandler(logging.ERROR)
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    
    
    logger.handlers = []
    logger.addHandler(console_handler)
    logger.addHandler(debug_file_handler)
    logger.addHandler(error_file_handler)
    
    