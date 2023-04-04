from bpy.types import Operator

def debug(message, op: Operator = None) -> None:
    print(f"PA [DEBUG] >> {message}\033[0m")
    if (op != None):
        op.report({ "DEBUG" }, message)

def info(message, op: Operator = None) -> None:
    print(f"PA [\033[96mINFO\033[0m]  >> {message}\033[0m")
    if (op != None):
        op.report({ "INFO" }, message)

def warn(message, op: Operator = None) -> None:
    print(f"PA [\033[93mWARN\033[0m]  >> {message}\033[0m")
    if (op != None):
        op.report({ "WARNING" }, message)

def error(message, op: Operator = None) -> None:
    print(f"PA [\033[91mERROR\033[0m] >> {message}\033[0m")
    if (op != None):
        op.report({ "ERROR" }, message)