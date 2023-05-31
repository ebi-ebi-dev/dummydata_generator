import logging
import logging.handlers

buckupCount = 7
fh = logging.handlers.TimedRotatingFileHandler("./dummydatagenerator/media/log/access.log", 
                                                when = 'Midnight', 
                                                # when = 'S', 
                                                backupCount = buckupCount
                                                )
fh.suffix = "%Y%m%d"
fh.setLevel(logging.DEBUG)
fh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
fh.setFormatter(fh_formatter)

class my_logger:
    def __init__(self) -> None:

        logger = logging.getLogger('access.log')
        logger.setLevel(logging.DEBUG)
        logger.addHandler(fh)

        self.logger = logger
    
    def info(self, msg):
        self.logger.info(msg)
    
    def error(self, msg):
        self.logger.error(msg)