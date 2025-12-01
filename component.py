import environment as e
from typing import Generator

def _print_center(text, fill=" "):
    width = e.SHELL_WIDTH
    print(text.center(width, fill))

def _print_main_view(nodes:tuple[Generator]):
    for gene in nodes:
        for g in gene:
            _print_center(g)


def print_view(nodes:tuple[Generator], line = "=" ,header = "", footer = ""):
    print(f"{line*e.SHELL_WIDTH}")
    print(header) if header!="" else print(end="")
    print("\n\n\n\n\n\n\n\n\n\n\n")

    _print_main_view(nodes)

    print("\n\n\n\n\n\n\n\n\n\n\n")
    print(footer) if footer!="" else print(end="")
    print(f"{line*e.SHELL_WIDTH}")

def text(*plots:str):
    """
    ＜p＞と同義
    """
    for p in plots:
        yield p

def e_box(*nodes:Generator, witdh:int = 30):
    """
    =で囲んだ文字列を返します
    """
    yield "="*witdh

    for gene in nodes:
        for g in gene:
            yield g

    yield "="*witdh
    

def selector(options:list[str],selecting:int): #generator
    """
    selector:選択肢の文字列を返します
    
    引数：{選択肢名:onSelect関数},選択番号
    """
    for i in range(len(options)):
        yield "⇨"+options[i] if selecting==i else " " + options[i]

def padding(value:int = 1):
    for v in range(value):
        yield "\n"