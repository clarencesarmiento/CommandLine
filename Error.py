import colorama
from colorama import Fore, Style

colorama.init()


def printline(text):
    return print(Fore.RED + text + Style.RESET_ALL)
