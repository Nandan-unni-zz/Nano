from colorama import Fore, Style

def err(field, err):
    return Fore.RED + Style.BRIGHT + "[ERR]  " + Style.RESET_ALL + Fore.YELLOW + f"{field}: " + Style.RESET_ALL + f"{err}"

def warn(msg):
    return Fore.YELLOW + msg + Style.RESET_ALL

def msg(field, msg):
    return Fore.YELLOW + Style.BRIGHT + f"[{field}]  " + Style.RESET_ALL + f"{msg}"

def log(field, head, body):
    clr = Fore.GREEN if field == 'REQ' else Fore.BLUE
    return clr + Style.BRIGHT + f"[{field}]  " + Style.RESET_ALL + Fore.YELLOW + f"{head}: " + Style.RESET_ALL + body

if __name__ == '__main__':
    print(warn("Testing logging system"))
    print(log("REQ", "POST", "/test/url"))
    print(log("RES", 200, "OK"))
    print(err("TEST", "Testing logging system"))
    print(msg("Testing logging system"))
