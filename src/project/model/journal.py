from configparser import ConfigParser
from loguru import logger
import logging


def debug_level(filename="config.ini", section="logger"):
    parser = ConfigParser()
    parser.read(filename)
    log_level = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            log_level[param[0]] = param[1]
    else:
        raise Exception('Section {0} is not found in the {1} file'.format(section, filename))
    return log_level.get(param[0])

class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())
