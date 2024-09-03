import argparse
from collections import deque

from parsers import btmlParser
from utils import mappings

def main():
    parser = argparse.ArgumentParser("BTML.py")
    parser.add_argument("file", help="The .btml file to be parsed")
    args = parser.parse_args()
    assert args.file[len(args.file)-5:] == ".btml", "Invalid File Type Passed (needs to be .btml)"
    res = "<!DOCTYPE html>\n<html>\n"

    with open(args.file, "r") as file:
        lines = file.readlines()
        res += btmlParser.parse(lines)

    res += "\n</html>"
    with open(f"{args.file[:len(args.file)-5]}.html", "w") as file:
        file.write(res)

if __name__ == "__main__":
    main()