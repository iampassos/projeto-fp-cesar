import os
import platform
import shutil

def is_int(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
    
def is_float(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")


columns, rows = shutil.get_terminal_size()


def centralizar_meio_inferior(text):
    columns, rows = shutil.get_terminal_size()
    x_position = (columns - len(text)) // 2

    return f"\033[{rows};{x_position}H{text}"


def texto_centralizado(text, abaixo=0):
    x_pos = columns // 2 - len(text) // 2
    y_pos = rows // 2 + abaixo
    print("\033[{0};{1}H{2}".format(y_pos, x_pos, text))


def textos_centralizados(*lines, acima=0):
    max_length = max(len(line) for line in lines)
    fixed_x_pos = columns // 2 - max_length // 2
    start_y_pos = rows // 2 - len(lines) - acima
    for i, text in enumerate(lines):
        y_pos = start_y_pos + i
        print("\033[{0};{1}H{2}".format(y_pos, fixed_x_pos, text))


def input_centralizado(text, abaixo=0):
    x_pos = columns // 2 - len(text) // 2
    y_pos = rows // 2 + abaixo
    print("\033[{0};{1}H{2}".format(y_pos, x_pos, text), end="")
    return input()
