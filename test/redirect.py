"""
Иногда возникает необходимость перенаправить вывод в нужное нам место внутри программы по ходу её выполнения.
Реализуйте контекстный менеджер, который принимает два IO-объекта (например, открытые файлы)
и перенаправляет туда стандартные потоки stdout и stderr.

Аргументы контекстного менеджера должны быть непозиционными,
чтобы можно было ещё перенаправить только stdout или только stderr.
"""

from types import TracebackType
from typing import Type, Literal, IO
import sys
import traceback


class Redirect:
    def __init__(self, *, stdout: IO = None, stderr: IO = None) -> None:
        self.stdout = stdout
        self.stderr = stderr

        self._orig_stdout = None
        self._orig_stderr = None

    def __enter__(self):
        self._orig_stderr = sys.stderr
        self._orig_stdout = sys.stdout

        if self.stdout:
            sys.stdout = self.stdout
        if self.stderr:
            sys.stderr = self.stderr

        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> Literal[True] | None:
        if exc_type is not None and self.stderr:
            traceback.print_exception(exc_type, exc_val, exc_tb, file=self.stderr)

        sys.stdout = self._orig_stdout
        sys.stderr = self._orig_stderr

        if self.stderr:
            return True

with open('out.txt', 'w', encoding='utf-8') as f1, open('err.txt', 'w', encoding='utf-8') as f2:
    with Redirect(stdout=f1, stderr=f2):
        print('In outoput')
        raise ValueError('in Err 4')