"""
Coding Interview: Toy Language Type System

Implement `type_check(program)` below.

  - Return "ok" if the whole program is well-typed.
  - Otherwise return a string describing the FIRST error (scanning top to bottom).
    Exact wording isn't graded, but it should clearly identify the problem,
    e.g. "type error: cannot apply + to int and string" or "undefined variable: b".

Types: "int", "bool", "string".

Operators:
  +  : int + int -> int, string + string -> string
  -  : int - int -> int
  == : operands must share a type; result is bool
  && : bool && bool -> bool

Rules:
  - A variable must be assigned before it is used.
  - A variable may be reassigned, and its type can change (latest `let` wins).

Run this file to check your implementation against the examples:  python toy_type_system.py
"""


# ---------------------------------------------------------------------------
# Data model  (already provided -- you do NOT need to parse raw text)
# ---------------------------------------------------------------------------

class Lit:
    """A literal value. `type` is one of "int", "bool", "string"."""
    def __init__(self, type, value):
        self.type = type
        self.value = value


class Var:
    """A reference to a previously assigned variable."""
    def __init__(self, name):
        self.name = name


class BinOp:
    """A binary operation. `op` is one of "+", "-", "==", "&&"."""
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Let:
    """Assignment statement:  let <name> = <expr>"""
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr


class Print:
    """Print statement:  print <expr>   (forces type-checking of expr)"""
    def __init__(self, expr):
        self.expr = expr


# ---------------------------------------------------------------------------
# YOUR SOLUTION GOES HERE
# ---------------------------------------------------------------------------


# Initialize a dictionary to store variable types
"""
program: a list of statements (Let / Print).
Returns "ok" or an error message string (see module docstring).

Operators:
    +  : int + int -> int, string + string -> string
    -  : int - int -> int
    == : operands must share a type; result is bool
    && : bool && bool -> bool

Rules:
    - A variable must be assigned before it is used.
    - A variable may be reassigned, and its type can change (latest `let` wins).
"""


class TypeError_(Exception):
    """Raised internally when an expression fails to type-check."""
    pass


def type_check(program):
    """
    program: a list of statements (Let / Print).
    Returns "ok" or an error message string (see module docstring).
    """
    env = {}  # variable name -> current type ("int" / "bool" / "string")

    def type_of(expr):
        if isinstance(expr, Lit):
            return expr.type

        if isinstance(expr, Var):
            if expr.name not in env:
                raise TypeError_(f"undefined variable: {expr.name}")
            return env[expr.name]

        if isinstance(expr, BinOp):
            left = type_of(expr.left)     # evaluate operands first (left to right)
            right = type_of(expr.right)
            return type_of_binop(expr.op, left, right)

        raise TypeError_(f"unknown expression: {expr!r}")

    def type_of_binop(op, left, right):
        if op == "+":
            if left == "int" and right == "int":
                return "int"
            if left == "string" and right == "string":
                return "string"
        elif op == "-":
            if left == "int" and right == "int":
                return "int"
        elif op == "==":
            if left == right:
                return "bool"
        elif op == "&&":
            if left == "bool" and right == "bool":
                return "bool"
        else:
            raise TypeError_(f"unknown operator: {op}")

        raise TypeError_(f"type error: cannot apply {op} to {left} and {right}")

    for statement in program:
        try:
            if isinstance(statement, Let):
                env[statement.name] = type_of(statement.expr)
            elif isinstance(statement, Print):
                type_of(statement.expr)
            else:
                return f"unknown statement: {statement!r}"
        except TypeError_ as err:
            return str(err)

    return "ok"
    



# ---------------------------------------------------------------------------
# Example programs
# ---------------------------------------------------------------------------

# Example 1 -- well-typed
#   let x = 1
#   let y = x + 2
#   let z = (y == 3)
#   print z && true
EXAMPLE_1 = [
    Let("x", Lit("int", 1)),
    Let("y", BinOp("+", Var("x"), Lit("int", 2))),
    Let("z", BinOp("==", Var("y"), Lit("int", 3))),
    Print(BinOp("&&", Var("z"), Lit("bool", True))),
]

# Example 2 -- type error: + on int and string
#   let x = 1
#   let y = "hi"
#   print x + y
EXAMPLE_2 = [
    Let("x", Lit("int", 1)),
    Let("y", Lit("string", "hi")),
    Print(BinOp("+", Var("x"), Var("y"))),
]

# Example 3 -- undefined variable: b
#   let a = b + 1
EXAMPLE_3 = [
    Let("a", BinOp("+", Var("b"), Lit("int", 1))),
]

# Example 4 -- reassignment changes type, still ok
#   let x = 1
#   let x = "now a string"
#   print x + "!"
EXAMPLE_4 = [
    Let("x", Lit("int", 1)),
    Let("x", Lit("string", "now a string")),
    Print(BinOp("+", Var("x"), Lit("string", "!"))),
]

# Example 5 -- nested expression, well-typed
#   let a = 5
#   let flag = true
#   print ((a - 1) == 0) && flag
EXAMPLE_5 = [
    Let("a", Lit("int", 5)),
    Let("flag", Lit("bool", True)),
    Print(
        BinOp("&&",
            BinOp("==",
                BinOp("-", Var("a"), Lit("int", 1)),
                Lit("int", 0)),
            Var("flag")),
    ),
]

# Example 6 -- type error: && on non-bool
#   let x = 1
#   print x && true
EXAMPLE_6 = [
    Let("x", Lit("int", 1)),
    Print(BinOp("&&", Var("x"), Lit("bool", True))),
]

# Example 7 -- type error: == on mismatched types
#   let ok = (1 == "one")
EXAMPLE_7 = [
    Let("ok", BinOp("==", Lit("int", 1), Lit("string", "one"))),
]


# (statements, description, is_ok)
#   is_ok == True  -> expect exactly "ok"
#   is_ok == False -> expect any non-"ok" error string
CASES = [
    (EXAMPLE_1, "well-typed program", True),
    (EXAMPLE_2, "+ on int and string", False),
    (EXAMPLE_3, "undefined variable b", False),
    (EXAMPLE_4, "reassignment changes type", True),
    (EXAMPLE_5, "nested expression", True),
    (EXAMPLE_6, "&& on non-bool", False),
    (EXAMPLE_7, "== on mismatched types", False),
]


# ---------------------------------------------------------------------------
# Test harness
# ---------------------------------------------------------------------------

def _run():
    passed = 0
    for program, description, expect_ok in CASES:
        try:
            result = type_check(program)
        except NotImplementedError:
            print("type_check is not implemented yet.")
            return
        except Exception as exc:  # your code shouldn't crash on valid input
            print(f"[CRASH] {description}: raised {type(exc).__name__}: {exc}")
            continue

        got_ok = (result == "ok")
        ok = (got_ok == expect_ok)
        passed += ok
        status = "PASS" if ok else "FAIL"
        expectation = '"ok"' if expect_ok else "an error"
        print(f"[{status}] {description}: expected {expectation}, got {result!r}")

    print(f"\n{passed}/{len(CASES)} cases passed.")


if __name__ == "__main__":
    _run()
