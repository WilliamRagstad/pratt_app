from ops import *
from lexer import Lexer, Token

# Expression is either a identifier, number, string, unary/binary expression, or function application.
class Expr:
    def pretty(self) -> str:
        raise NotImplementedError("Subclasses must implement pretty() method")

class IdentifierExpr(Expr):
    def __init__(self, name: str):
        self.name = name
    def pretty(self) -> str:
        return self.name

class NumberExpr(Expr):
    def __init__(self, value: float):
        self.value = value
    def pretty(self) -> str:
        if self.value.is_integer():
            return str(int(self.value))
        return str(self.value)

class StringExpr(Expr):
    def __init__(self, value: str):
        self.value = value
    def pretty(self) -> str:
        return f'"{self.value}"'

class UnaryExpr(Expr):
    def __init__(self, op: str, expr: Expr):
        self.op = op
        self.expr = expr
    def pretty(self) -> str:
        return f"{self.op}{self.expr.pretty()}"

class BinaryExpr(Expr):
    def __init__(self, left: Expr, op: str, right: Expr):
        self.left = left
        self.op = op
        self.right = right
    def pretty(self) -> str:
        return f"({self.left.pretty()} {self.op} {self.right.pretty()})"

class AppExpr(Expr):
    def __init__(self, func: Expr, arg: Expr):
        self.func = func
        self.arg = arg
    def pretty(self) -> str:
        return f"({self.func.pretty()} {self.arg.pretty()})"

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer

    def parse_primary(self) -> Expr:
        nt: Token | None = self.lexer.next()
        if nt is None: raise ValueError("Unexpected end of input")
        elif nt.is_operator(): return UnaryExpr(nt.value, self.parse_primary())
        elif nt.is_identifier(): return IdentifierExpr(nt.value)
        elif nt.is_number(): return NumberExpr(nt.value)
        elif nt.is_string(): return StringExpr(nt.value)
        elif nt.is_left_paren():
            expr = self.parse_expr()
            nnt = self.lexer.next()
            if nnt is None or not nnt.is_right_paren(): raise ValueError("Expected right parenthesis")
            return expr
        else:
            raise ValueError(f"Unexpected token: {nt}")

    # Pratt parser for expressions with precedence
    def parse_expr(self, min_prec: int = 0) -> Expr:
        expr = self.parse_primary()
        while True:
            nt: Token | None = self.lexer.peek()
            if nt is None or nt.is_right_paren(): break # End of expression
            elif nt.is_operator():
                op = nt.value
                op_prec = BINARY_OPERATORS[op]
                if op_prec < min_prec: break # Do not bind louser
                self.lexer.next() # Consume operator
                rhs = self.parse_expr(op_prec)
                expr = BinaryExpr(expr, op, rhs)
            elif FUNCTION_APPLICATION > min_prec: # Often always true
                expr = AppExpr(expr, self.parse_primary())
            else: break # End of expression
        return expr

