from collections import deque
from utils import mappings

def parse(lines: list[str]) -> str:
    stack = deque()
    res = ""
    for i in lines:
        symbols = list(filter(None, [j.strip() for j in i.strip().split("{")]))
        for i in symbols:
            if i == "}":
                pass
            elif i in mappings:
                pass
            else:
                pass
    return res