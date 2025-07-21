"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""

from typing import Any, Optional

from flask_wtf import FlaskForm
from wtforms import Field, ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):
    def _len_number(form, field):
        lenght = len(str(field.data))
        if not (min < lenght <= max):
            error_message = (
                message or f"Длина должна быть от {min + 1} до {max} символов"
            )
            raise ValidationError(error_message)

    return _len_number


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field) -> Any:
        print(len(str(field.data)))
        if not self.min < len(str(field.data)) <= self.max:
            raise ValidationError(f"{self.message}")
