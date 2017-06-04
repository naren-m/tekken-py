import logging
import logging.handlers

LOG_FILENAME = 'logs/application.log'
FORMAT = '%(asctime)s-%(levelname).4s-%(filename)s:%(lineno).3d-%(funcName)s() : %(message)s'


var = ('\n'
	   'Level   Numeric value\n'
	   'CRITICAL    50\n'
	   'ERROR   	40\n'
	   'WARNING 	30\n'
	   'INFO    	20\n'
	   'DEBUG   	10\n'
	   'NOTSET  	0\n')

# Default logger
app_logger = logging.getLogger(__name__)

info = app_logger.info
debug = app_logger.debug
warning = app_logger.warning
error =  app_logger.error
critical = app_logger.critical
log = app_logger.log
exception = app_logger.exception

def getLogger(printToScreen=False):

    logging.basicConfig(filename=LOG_FILENAME,
                        format= FORMAT,
                        level=logging.DEBUG,
                        datefmt='%m/%d/%Y %I:%M:%S')

    
    if printToScreen:
        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter(FORMAT)
        console.setFormatter(formatter)
        logging.getLogger(__name__).addHandler(console)

    app_logger = logging.getLogger(__name__)

    return app_logger