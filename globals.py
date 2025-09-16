DEBUG_MODE: bool = False
WAIT_TIME: float = 0.1
START_TIME: float

def debug(msg: str) -> None:
    if DEBUG_MODE: print(f'DEBUG - {msg}')

