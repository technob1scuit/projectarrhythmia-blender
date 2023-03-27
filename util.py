def debug(message) -> None:
    print(f"PA [DEBUG] >> {message}\033[0m")

def info(message) -> None:
    print(f"PA [\033[96mINFO\033[0m]  >> {message}\033[0m")

def warn(message) -> None:
    print(f"PA [\033[93mWARN\033[0m]  >> {message}\033[0m")

def error(message) -> None:
    print(f"PA [\033[91mERROR\033[0m] >> {message}\033[0m")