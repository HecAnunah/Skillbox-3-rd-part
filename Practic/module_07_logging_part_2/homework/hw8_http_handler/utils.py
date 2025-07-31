from typing import Union, Callable
from operator import sub, mul, truediv, add
from httpHandler import get_logger

logger = get_logger("server")


OPERATORS = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
}

Numeric = Union[int, float]


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    logger.info(f"Entering in fucn string_to_operator")
    if not isinstance(value, str):
        logger.error(f"wrong operator type, {value}")
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        logger.warning(f"wrong operator value, {value}")
        raise ValueError("wrong operator value")
    logger.critical("Test critical")
    logger.warning("Test warning")
    logger.debug("Test debug")
    return OPERATORS[value]
