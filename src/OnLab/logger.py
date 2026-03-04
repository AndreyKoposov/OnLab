"""logging"""
from logging import getLogger, DEBUG, Formatter
from logging.handlers import RotatingFileHandler


class LogManager():
    """Класс, отвечающий за логгирование"""
    logger = getLogger(__name__)

    @staticmethod
    def start(path: str) -> None:
        """Запускает работу логгера"""
        LogManager.logger.setLevel(DEBUG)

        formatter = Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler = RotatingFileHandler(
            path + 'logs\\app.log',
            maxBytes=1024*1024,
            encoding='utf-8'
        )
        file_handler.setLevel(DEBUG)
        file_handler.setFormatter(formatter)

        LogManager.logger.addHandler(file_handler)
        LogManager.logger.info('Started')

    @staticmethod
    def info(msg):
        """Log inof message"""
        LogManager.logger.info(msg)

    @staticmethod
    def error(msg):
        """Log inof message"""
        LogManager.logger.error(msg)
