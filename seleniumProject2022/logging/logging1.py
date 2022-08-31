import logging

logging.basicConfig(filename='C://Projects//pythonSelenium//logs//testLog.log',
                    format= '%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S:%p',
                    level=logging.DEBUG
                                        )

    logging.debug(' this is a DEBUG message')
    logging.info(' this is a Info message')
    logging.warning(' this is a Warning  message')
    logging.error(' this is a ERROR message')
    logging.critical(' this is a Critical message')


