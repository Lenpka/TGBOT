import logging
logging.error("ТЕСТИРУЕМ ЛОГИ")
logging.debug("ЭТО ДЕБАГ")
logging.basicConfig(level=logging.CRITICAL)
logging.info("ВСЕ НОРМА")
logging.critical("НЕ НОРМА \n")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.debug('меня не существует?')
logger.warning('А Я ЕСТЬ!')