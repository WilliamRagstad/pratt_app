#!/bin/env python3

from lexer import Lexer
from parser import Parser

RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def main():
    while True:
        try:
            source = input(f"{YELLOW}>{RESET} ").strip()
            if source == "": continue
            expr = Parser(Lexer(source)).parse_expr()
            print(expr.pretty())
        except KeyboardInterrupt: break
        except Exception as e:
            print(f"{RED}error{RESET}: {e}")
            break

if __name__ == "__main__":
    main()
