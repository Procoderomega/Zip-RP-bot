from colorama import Fore, init, Style

init(autoreset=True)

OK = f"[{Fore.GREEN}OK{Style.RESET_ALL}]"
DEBUG = f"[{Fore.YELLOW}DEBUG{Style.RESET_ALL}]"
FAIL = f"[{Fore.RED}FAIL{Style.RESET_ALL}]"