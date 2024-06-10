import os
import datetime
import colorama
import atexit
import sys
import traceback
from colorama import Fore
from enum import Enum

colorama.init()

class LogLevel(Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4
    FATAL = 5

# Default values
min_log_level = LogLevel.INFO
auto_error_logging: bool = True
log_location: str = "logs"
title_timestamp_format: str = "%y-%m-%d-%H-%M"
short_timestamp_format: str = "%H:%M:%S"
log_format: str = "[{timestamp}] [{level}] [{source}]: {message}"
latest_log_name: str = "latest"

levelColors = {
    LogLevel.INFO: Fore.CYAN,
    LogLevel.WARNING: Fore.YELLOW,
    LogLevel.ERROR: Fore.LIGHTRED_EX,
    LogLevel.CRITICAL: Fore.MAGENTA,
    LogLevel.FATAL: Fore.RED
}

log_buffer = []

def get_title_timestamp() -> str:
    """
    Returns the current timestamp formatted as a title.
    """
    format = title_timestamp_format
    return datetime.datetime.now().strftime(format)

def get_timestamp() -> str:
    """
    Returns the current timestamp formatted as a short timestamp.
    """
    return datetime.datetime.now().strftime(short_timestamp_format)

def plain_log(message: str, source: str, level: LogLevel) -> None:
    """
    Logs a message with the specified source and log level.

    Args:
        message (str): The message to log.
        source (str): The source of the log message.
        level (LogLevel): The log level.

    Returns:
        None
    """
    if level.value < min_log_level.value:
        return

    log_message = log_format.format(timestamp=get_timestamp(), level=level.name, source=source, message=message)
    print(f"{levelColors[level]}{log_message}{Fore.RESET}\n")
    log_buffer.append(log_message)

def logInfo(message: str, source: str) -> None:
    """
    Logs an informational message with the specified source.

    Args:
        message (str): The message to log.
        source (str): The source of the log message.

    Returns:
        None
    """
    plain_log(message, source, LogLevel.INFO)

def logWarning(message: str, source: str) -> None:
    """
    Logs a warning message with the specified source.

    Args:
        message (str): The message to log.
        source (str): The source of the log message.

    Returns:
        None
    """
    plain_log(message, source, LogLevel.WARNING)

def logError(message: str, source: str) -> None:
    """
    Logs an error message with the specified source.

    Args:
        message (str): The message to log.
        source (str): The source of the log message.

    Returns:
        None
    """
    plain_log(message, source, LogLevel.ERROR)

def logCritical(message: str, source: str) -> None:
    """
    Logs a critical message with the specified source.

    Args:
        message (str): The message to log.
        source (str): The source of the log message.

    Returns:
        None
    """
    plain_log(message, source, LogLevel.CRITICAL)

def logFatal(message: str, source: str) -> None:
    """
    Logs a fatal message with the specified source.

    Args:
        message (str): The message to log.
        source (str): The source of the log message.

    Returns:
        None
    """
    plain_log(message, source, LogLevel.FATAL)

import traceback

def log_exception(e: Exception, level: LogLevel = LogLevel.ERROR, source: str = "Main"):
    """
    Logs an exception with its stack trace.

    Args:
        e (Exception): The exception to log.
        level (LogLevel, optional): The log level. Defaults to LogLevel.ERROR.
        source (str, optional): The source of the log message. Defaults to "Main".

    Returns:
        None
    """
    stack_trace = traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__)
    stack_trace_str = "".join(stack_trace)

    log(f"Exception: {str(e)}\n{stack_trace_str}", level, source)

def flush_logs() -> None:
    """
    Flushes the log buffer to a log file.

    Returns:
        None
    """
    if log_location and log_buffer:
        os.makedirs(log_location, exist_ok=True)
        log_file_path = os.path.join(log_location, latest_log_name+".txt")

        if os.path.exists(log_file_path):
            timestamp = get_title_timestamp()
            pid = os.getpid()
            new_file_path = os.path.join(log_location, f"{timestamp}_{pid}.txt")
            os.rename(log_file_path, new_file_path)

        with open(log_file_path, "w") as f:
            f.writelines(log_buffer)

atexit.register(flush_logs)

def handle_uncaught_exception(exc_type, exc_value, exc_traceback) -> None:
    """
    Handles uncaught exceptions by logging the exception details.

    Args:
        exc_type (type): The type of the exception.
        exc_value (Exception): The exception instance.
        exc_traceback (traceback): The traceback object.

    Returns:
        None
    """
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    formatted_traceback = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))

    print(formatted_traceback)

    logError(f"Uncaught exception: {exc_value}\n{formatted_traceback}", "UnhandledException")
    log_buffer.append(formatted_traceback)

if auto_error_logging:
    sys.excepthook = handle_uncaught_exception