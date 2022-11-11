import logging


class LogGen:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename="./Logs/app.log",
                            format='%(asctime)s %(name)s %(levelname)s:%(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            filemode="w",
                            level=logging.DEBUG
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
