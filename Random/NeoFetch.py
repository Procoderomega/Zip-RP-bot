import platform
import discord
from colorama import Fore, Style, init

init(autoreset=True)

def botfetch(bot):

    ascii_art = r"""::::::::::::::::::::::::-==--::::::::::::::::
::::::::::::::::::::::::+--++=--:::::::::::::
:::::::::::::::::::::::-=--==--=-::::::::::::
::::::::::::--+=--::-++----+--++--:::::::::::
:::::::------+*+**#**+**+----=*--::::::::::::
:::::::-==-------::--=#%@@@@@%*=-------::::::
::::------==------=--+%@@@@@@@@@@@%###*-:::::
:::--++++=--::--=--+--+@@@@@@@@@@@@@@%=::::::
:-=++=---------=--+*--*@@@@@@@@@@@@@@*-::::::
:-+-----:===++==+#@%-=*#%%##@@@@@@@@@+==-::::
:---==+=---***#@@@@%%%**@@@=@@@@@@@@@%%#-::::
:::-++---:-=#@@@@@@@##*****-+#@%@@@@%%*-----:
::-=+-=++++%#%@#=----==-----+%%@%#=*+=+##*+-:
::-=++=--=-=*+=*+---=---+-=#*+==**=-----++--:
:::----:::-------+*+++++*+-#*------::--=++*--
:::::::::::::::::---=++=++++%=----:::-=+===-:
::::::::::::::::-++----------*%******+=----::
::::::::::::::-=**+=--=+=+-:*--*#*----:::::::
::::::::::::--*+---=*######==++=-+%%*--::::::
:::::::::::-+#++***==--++==-#+#**#*+-*%=-::::
:::::::::-=*--=+*+=--=****=-##+***++=+*+--:::
::::::::::-+*+==------------=+=**=----:::::::
::::::::::::::---=+**#####*+==---::::::::::::""".splitlines()

    info = [
        "──── ZIP ^w^ BOT SYSTEM INFO ────",
        "",
        f"Bot Name      : {bot.user}",
        f"Python        : {platform.python_version()}",
        f"discord.py    : {discord.__version__}",
        f"Servers       : {len(bot.guilds)}",
        f"Cogs Loaded   : {len(bot.cogs)}",
        f"Latency       : {round(bot.latency*1000)}ms",
        "",
        f"{Fore.YELLOW}OS            : {Style.RESET_ALL}{platform.system()} {platform.release()}",
        f"{Fore.YELLOW}Arch          : {Style.RESET_ALL}{platform.machine()}",
    ]

    width = 50  # ancho reservado para el ascii

    for i in range(max(len(ascii_art), len(info))):

        left = ascii_art[i] if i < len(ascii_art) else ""
        right = info[i] if i < len(info) else ""

        print(Fore.WHITE + left.ljust(width) + Style.RESET_ALL + right)

    print()