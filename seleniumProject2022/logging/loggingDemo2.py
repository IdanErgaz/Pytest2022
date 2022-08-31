import logging

logging.basicConfig(filename='C://Projects//pythonSelenium//logs//testLog.log',
                    format= '%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S:%p'
                                        )

logger= logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug('this is a debug message')
logger.info('this is an info message')
logger.error('this is an error message')
logger.warning('this is a warning message')
logger.critical('that\'s a critical message')
