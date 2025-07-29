import logging
import time

import requests

# Без этого импорта не будет работать наследования в логировании: utils.http_utils
import logger


logger = logging.getLogger('utils.http_utils')
logger.setLevel(logging.INFO)
print(logger.parent) # Смена родителя в логгере по имени
print('*' * 40)
print("Эффективный уровень:", logging.getLevelName(logger.getEffectiveLevel()))
print("Handlers текущего логгера:", logger.handlers)
print("Наследует обработчики?", logger.propagate)
print("Родитель логгера:", logger.parent)
print("Имя родителя:", logger.parent.name)
print("Handlers родителя:", logger.parent.handlers)






GET_IP_URL = 'https://api.ipify.org?format=json'


def get_ip_address() -> str:
    logger.debug('Start getting IP address')
    start = time.time()
    try:
        ip = requests.get(GET_IP_URL).json()['ip']
    except Exception as e:
        logger.exception(e)
        raise e
    logger.debug('Done requesting ip in {:.4f} seconds'.format(time.time() - start))
    logger.info('Ip address: {}'.format(ip))
    return ip
