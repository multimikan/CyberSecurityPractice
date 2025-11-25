import environment as e

def _print_center(text, fill=" "):
    width = e.SHELL_WIDTH
    print(text.center(width, fill))

def my_print(s:tuple, line = "=" ,header = "", footer = ""):
    print(f"{line*e.SHELL_WIDTH}")
    print(header) if header!="" else print(end="")

    for _s in s:
        _print_center(_s)

    print(footer) if footer!="" else print(end="")
    print(f"{line*e.SHELL_WIDTH}")