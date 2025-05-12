# Pratt Parser Application

This example project implements a Pratt parser with support for **function application**, **unary** and **binary** operators, and a streaming lexer for tokenizing input.
The parsed expressions are based on **operator precedence**.

## Features

- **Lexer**: Tokenizes input strings into identifiers, numbers, strings, operators, and parentheses.
- **Parser**: Implements a Pratt parsing algorithm to handle expressions with precedence and associativity.
- **Expression Types**:
  - Identifiers
  - Numbers
  - Strings
  - Unary expressions
  - Binary expressions
  - Function applications
- **Operator Precedence**: Configurable precedence levels for unary and binary operators.
- **Interactive REPL**: A command-line interface for evaluating expressions.

## Usage

1. Clone the repository.
2. Run the `main.py` script to start the REPL:

   ```bash
    > 1+2*3
    (1 + (2 * 3))

    > 1*2+3
    ((1 * 2) + 3)

    > float pi = 3.14
    ((float pi) = 3.14)

    > int func x y z = x * 2 + z^2 - 10
    (((((int func) x) y) z) = ((x * 2) + ((z ^ 2) - 10)))

    > print x y z
    (((print x) y) z)
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
