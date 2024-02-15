import sys
from typing import Type, Any, Tuple


def exception_detail(error: Type[Exception], error_detail: Any) -> str:
    """
    Create a detailed error message including file name, line number, and error message.

    :param error: The exception type
    :param error_detail: The exception details (sys.exc_info())
    :return: Detailed error message
    """
    _, _, exc_tb = error_detail  # It returns a tuple (exc_type, exc_value, exc_traceback)

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in Python script: {} at line {}: {}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class AppException(Exception):
    """
    Custom exception class with additional details.
    """

    def __init__(self, error_message: str, error_detail: Any):
        """
        :param error_message: Error message in string format
        :param error_detail: The exception details (sys.exc_info())
        """
        super().__init__(error_message)

        self.error_message = exception_detail(
            error=error_message, error_detail=error_detail
        )

    def __str__(self) -> str:
        """
        Return the detailed error message.
        """
        return self.error_message
