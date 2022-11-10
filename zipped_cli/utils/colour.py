from pyfiglet import figlet_format
from colorama import Fore, Style

def PrintFiglet(text: str):
    print(figlet_format(text))

def printGreen(text: str):
    print(Fore.GREEN + text)
    print(Style.RESET_ALL)

def printRed(text: str):
    print(Fore.RED + text)
    print(Style.RESET_ALL)

def printYellow(text: str):
    print(Fore.YELLOW+ text)
    print(Style.RESET_ALL)