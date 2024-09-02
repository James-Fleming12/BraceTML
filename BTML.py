import argparse
from utils import Mappings

def main():
    parser = argparse.ArgumentParser("BTML.py")
    parser.add_argument("file", help="The .btml file to be parsed")
    args = parser.parse_args()
    assert args.file[len(args.file)-5:] == ".btml", "Invalid File Type Passed (needs to be .btml)"
    res = ""

    with open(args.file) as file:
        pass

if __name__ == "__main__":
    main()