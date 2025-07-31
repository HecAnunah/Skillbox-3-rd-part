import logging


class ASCIIFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        msg = record.getMessage()
        # return msg.isascii()  # Метод с str.isascii()
        return all(ord(sym) < 128 for sym in msg)  # своя проверка
