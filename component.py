import environment as e

def _print_center(text, fill=" "):
    width = e.SHELL_WIDTH
    print(text.center(width, fill))

def my_print(s:tuple, line = "="):
    print(f"{line*e.SHELL_WIDTH}")
    for _s in s:
        _print_center(_s)