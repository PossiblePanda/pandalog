import os
import datetime
import colorama
import atexit
from colorama import Fore
from enum import Enum

log_location: str = "logs"
colorama.init()

class LogLevel(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
    FATAL = "FATAL"

levelColors = {
    LogLevel.INFO: Fore.CYAN,
    LogLevel.WARNING: Fore.YELLOW,
    LogLevel.ERROR: Fore.LIGHTRED_EX,
    LogLevel.CRITICAL: Fore.MAGENTA,
    LogLevel.FATAL: Fore.RED
}

log_buffer = []

def get_timestamp(include_seconds: bool = False) -> str:
    format = "%y-%m-%d-%H-%M-%S" if include_seconds else "%y-%m-%d-%H-%M"
    return datetime.datetime.now().strftime(format)

def get_timestamp_short() -> str:
    return datetime.datetime.now().strftime("%H:%M:%S")

def log(message: str, source: str, level: LogLevel) -> None:
    print(f"{levelColors[level]} [{get_timestamp_short()}] [{level.name}] [{source}] {message}{Fore.RESET}\n")
    log_buffer.append(f"[{get_timestamp_short()}] [{level.name}] [{source}] {message}\n")

def logInfo(message: str, source: str) -> None:
    log(message, source, LogLevel.INFO)

def logWarning(message: str, source: str) -> None:
    log(message, source, LogLevel.WARNING)

def logError(message: str, source: str) -> None:
    log(message, source, LogLevel.ERROR)

def logCritical(message: str, source: str) -> None:
	log(message, source, LogLevel.CRITICAL)

def logFatal(message: str, source: str) -> None:
	log(message, source, LogLevel.FATAL)

def flush_logs():
    if log_location and log_buffer:
        os.makedirs(log_location, exist_ok=True)  # Create the directory if it doesn't exist
        log_file_path = os.path.join(log_location, "latest.txt")

        if os.path.exists(log_file_path):
            timestamp = get_timestamp()
            new_file_path = os.path.join(log_location, f"{timestamp}.txt")
            os.rename(log_file_path, new_file_path)

        with open(log_file_path, "w") as f:
            f.writelines(log_buffer)
            
atexit.register(flush_logs)