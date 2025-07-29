import logging

logging.basicConfig()
logger = logging.getLogger()

logger_main = logging.getLogger('main')
logger_main.setLevel(logging.INFO)

logger_utils = logging.getLogger('utils')
logger_utils.setLevel(logging.DEBUG)