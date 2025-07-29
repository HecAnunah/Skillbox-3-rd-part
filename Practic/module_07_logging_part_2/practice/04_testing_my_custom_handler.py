import logging
import logging.config
from custom_handler import dict_config

logging.config.dictConfig(dict_config)

logger = logging.getLogger('with_my_handl')

# extra={'very': 'much'} этот атрибут позволяет дописывать сообщение в форматер если там указан ключ %(very)s
logger.debug('msg', extra={'very': 'much'})