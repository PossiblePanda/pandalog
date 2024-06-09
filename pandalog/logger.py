import os
import datetime

log_location: str = "logs"

def get_timestamp(include_seconds: bool = False) -> str:
    format = "%y-%m-%d-%H-%M-%S" if include_seconds else "%y-%m-%d-%H-%M"
    return datetime.datetime.now().strftime(format)

def log(message: str, source: str) -> None:
    print(f"[{source}] {message}")

    if not log_location:
        return

    os.makedirs(log_location, exist_ok=True)  # Create the directory if it doesn't exist

    log_file_path = os.path.join(log_location, "latest.txt")
    if not os.path.exists(log_file_path):
        with open(log_file_path, "a") as f:
            f.write(f"[{source}] {message}\n")
        return

    timestamp = get_timestamp()
    new_file_path = os.path.join(log_location, f"{timestamp}.txt")
    if os.path.exists(new_file_path):
        timestamp = get_timestamp(include_seconds=True)
        new_file_path = os.path.join(log_location, f"{timestamp}.txt")

    os.rename(log_file_path, new_file_path)

    with open(log_file_path, "a") as f:
        f.write(f"[{source}] {message}\n")