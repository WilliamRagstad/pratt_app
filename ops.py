UNARY_OPERATORS = ["!", "~", "-"]

# Higher precedence bind tighter
BINARY_OPERATORS = {
    ";": 1, # Statement separator
    "=": 10, # Assignment
    ",": 15, # Comma separator
    "&&": 20, # Logical AND
    "||": 20, # Logical OR
    "<": 30, # Less than
    ">": 30, # Greater than
    "<=": 30, # Less than or equal
    ">=": 30, # Greater than or equal
    "==": 30, # Equal
    "!=": 30, # Not equal
    "<<": 40, # Left shift
    ">>": 40, # Right shift
    "+": 50, # Addition
    "-": 50, # Subtraction
    "*": 60, # Multiplication
    "/": 60, # Division
    "%": 60, # Modulus
    "^": 70, # Exponentiation
}

ALL_OPERATORS = list(BINARY_OPERATORS.keys()) + UNARY_OPERATORS

# Stronger than all binary operators
FUNCTION_APPLICATION = 80
