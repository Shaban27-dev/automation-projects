from datetime import datetime

def log_error(error):
    with open("error.log", "a") as f:
        f.write(f"[ERROR] {datetime.now()} - {type(error).__name__}: {error}\n")