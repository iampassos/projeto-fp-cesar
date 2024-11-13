import os
import platform
import shutil


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


columns, rows = shutil.get_terminal_size()


def texto_centralizado(text, abaixo=0):
    x_pos = columns // 2 - len(text) // 2
    y_pos = rows // 2 + abaixo
    print("\033[{0};{1}H{2}".format(y_pos, x_pos, text))


def input_centralizado(text, abaixo=0):
    x_pos = columns // 2 - len(text) // 2
    y_pos = rows // 2 + abaixo
    print("\033[{0};{1}H{2}".format(y_pos, x_pos, text), end="")
    return input()
