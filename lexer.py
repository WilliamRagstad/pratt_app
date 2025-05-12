
# Token is either a identifier, number, string, operator, or parenthesis.
from ops import ALL_OPERATORS
from typing import Callable

class Token:
    def __init__(self, type: str, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return f"{self.type}({self.value})"

    @staticmethod
    def identifier(value: str) -> 'Token':
        return Token("identifier", value)
    @staticmethod
    def number(value: float) -> 'Token':
        return Token("number", value)
    @staticmethod
    def string(value: str) -> 'Token':
        return Token("string", value)
    @staticmethod
    def op(value: str) -> 'Token':
        return Token("op", value)
    @staticmethod
    def paren(kind: str) -> 'Token':
        return Token("paren", kind)

    def is_identifier(self) -> bool:
        return self.type == "identifier"
    def is_number(self) -> bool:
        return self.type == "number"
    def is_string(self) -> bool:
        return self.type == "string"
    def is_operator(self) -> bool:
        return self.type == "op"
    def is_left_paren(self) -> bool:
        return self.type == "paren" and self.value == "("
    def is_right_paren(self) -> bool:
        return self.type == "paren" and self.value == ")"

class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.peek_queue = []

    def read_while(self, condition: Callable[[str], bool]) -> str:
        result = ""
        while self.pos < len(self.source) and condition(self.source[self.pos]):
            result += self.source[self.pos]
            self.pos += 1
        return result

    def __next_token(self) -> Token | None:
        if self.pos >= len(self.source): return None
        cc = self.source[self.pos]
        if cc.isspace():
            self.read_while(str.isspace)
            return self.__next_token()
        elif cc.isdigit() or cc == '.': return Token.number(float(self.read_while(lambda c: str.isdigit(c) or c == '.')))
        elif cc.isalpha(): return Token.identifier(self.read_while(str.isalnum))
        elif cc in "()":
            self.pos += 1
            return Token.paren(cc)
        elif cc in "\"'":
            self.pos += 1
            t = Token.string(self.read_while(lambda c: c != cc))
            self.pos += 1
            return t
        elif cc in "".join(ALL_OPERATORS):
            MAX_OP_LEN = max(len(op) for op in ALL_OPERATORS)
            for length in range(MAX_OP_LEN, 0, -1):
                if self.pos + length > len(self.source): continue # Out of bounds
                op = self.source[self.pos:self.pos+length]
                if op in ALL_OPERATORS:
                    self.pos += length
                    return Token.op(op)
        raise ValueError(f"Unexpected character: {cc}")

    def next(self) -> Token | None:
        if len(self.peek_queue) > 0:
            return self.peek_queue.pop(0)
        return self.__next_token()

    def peek(self, offset: int = 0) -> Token | None:
        while len(self.peek_queue) <= offset:
            token = self.__next_token()
            if token is None: break
            self.peek_queue.append(token)
        if offset < len(self.peek_queue): return self.peek_queue[offset]
        else: return None
