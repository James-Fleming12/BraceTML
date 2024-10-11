from collections import deque
from utils import Mappings

def parse(lines: list[str]) -> str:
    stack = deque()
    mappings = Mappings.mappings();
    res = ""
    for i in lines:
        symbols = list(filter(None, [j.strip() for j in i.strip().split("{")]))
        for i in symbols:
            if i == "}":
                res += "\t"*(len(stack)-1) + stack.pop() + "\n"
            elif i in mappings:
                res += "\t"*len(stack) + mappings[i][0] + "\n"
                stack.append(mappings[i][1])
            else:
                for m in i.split(" "): 
                    if m == "": continue
                    if m.strip() == "}": res += "\n" + "\t"*(len(stack)-1) + stack.pop() + "\n" ; continue
                    res += "\t"*len(stack) + m.strip()
    return res