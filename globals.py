DEBUG_MODE: bool = True
START_TIME: float

def debug(msg: str) -> None:
    if DEBUG_MODE: print(f'DEBUG - {msg}')

