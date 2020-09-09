import logging


class Logger:
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename="result.log",
                        format='%(name)s - %(levelname)s - %(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO,
                        )

    def __init__(self, filename):
        self.log = logging
        self.log = logging.getLogger(filename)

    def write_info(self, var):
        self.log.info(var)

    def write_warning(self, var):
        self.log.warning(var)

    def write_error(self, var):
        self.log.error(var)
