import logging

class Log:

    @staticmethod
    def get_logger():
        # Config Logger
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Create custom logger
        logger = logging.getLogger(__name__)
        return logger