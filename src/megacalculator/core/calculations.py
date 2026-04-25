from __future__ import annotations

import ast
import math
import operator
from decimal import Decimal, InvalidOperation, getcontext

getcontext().prec = 40

Number = int | float

_BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_UNARY_OPS = {ast.UAdd: operator.pos, ast.USub: operator.neg}
_FUNCTIONS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
    "log": math.log10,
    "ln": math.log,
    "abs": abs,
}
_CONSTANTS = {"pi": math.pi, "e": math.e}


def add(x: Number, y: Number) -> float:
    return float(x + y)


def subtract(x: Number, y: Number) -> float:
    return float(x - y)


def multiply(x: Number, y: Number) -> float:
    return float(x * y)


def divide(x: Number, y: Number) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return float(x / y)


def floor_division(x: Number, y: Number) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return float(x // y)


def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("Factorial needs a whole number.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)


def fibonacci(count: int) -> list[int]:
    if count < 1:
        raise ValueError("Count must be at least 1.")
    values: list[int] = []
    a, b = 0, 1
    for _ in range(count):
        values.append(a)
        a, b = b, a + b
    return values


def primes(count: int, start: int = 2) -> list[int]:
    if count < 1:
        raise ValueError("Count must be at least 1.")
    found: list[int] = []
    candidate = max(2, start)
    while len(found) < count:
        if is_prime(candidate):
            found.append(candidate)
        candidate += 1
    return found


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    limit = int(math.sqrt(value)) + 1
    for divisor in range(3, limit, 2):
        if value % divisor == 0:
            return False
    return True


def pi_leibniz(iterations: int = 100_000) -> float:
    if iterations < 1:
        raise ValueError("Iterations must be at least 1.")
    total = 0.0
    sign = 1.0
    for i in range(iterations):
        total += sign / (2 * i + 1)
        sign *= -1
    return 4 * total


def euler_limit(n: int) -> float:
    if n < 1:
        raise ValueError("n must be at least 1.")
    return float((Decimal(1) + (Decimal(1) / Decimal(n))) ** n)


def binomial_one_plus_x(x: Number, n: int) -> float:
    if n < 0:
        raise ValueError("Power must be zero or higher.")
    return float((1 + x) ** n)


def digit_parts(value: int) -> list[int]:
    if value < 0:
        raise ValueError("Digit writer needs a positive whole number.")
    return [int(char) for char in str(value)]


def trig_from_angle(function_name: str, angle: Number, degrees: bool = True) -> float:
    radians = math.radians(angle) if degrees else float(angle)
    if function_name == "sin":
        return math.sin(radians)
    if function_name == "cos":
        return math.cos(radians)
    if function_name == "tan":
        return math.tan(radians)
    if function_name == "cosec":
        return divide(1, math.sin(radians))
    if function_name == "sec":
        return divide(1, math.cos(radians))
    if function_name == "cot":
        return divide(1, math.tan(radians))
    raise ValueError(f"Unknown trigonometric function: {function_name}.")


def evaluate_expression(expression: str) -> float:
    normalized = (
        expression.replace("×", "*")
        .replace("÷", "/")
        .replace("^", "**")
        .replace("%", "/100")
    )
    if not normalized.strip():
        raise ValueError("Enter an expression first.")
    try:
        tree = ast.parse(normalized, mode="eval")
        return float(_eval_node(tree.body))
    except (SyntaxError, ValueError, TypeError, ZeroDivisionError, InvalidOperation) as exc:
        raise ValueError("That expression cannot be calculated.") from exc


def _eval_node(node: ast.AST) -> float:
    if isinstance(node, ast.Constant) and isinstance(node.value, int | float):
        return float(node.value)
    if isinstance(node, ast.Name) and node.id in _CONSTANTS:
        return _CONSTANTS[node.id]
    if isinstance(node, ast.BinOp) and type(node.op) in _BIN_OPS:
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        if isinstance(node.op, (ast.Div, ast.FloorDiv, ast.Mod)) and right == 0:
            raise ValueError("Cannot divide by zero.")
        return float(_BIN_OPS[type(node.op)](left, right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPS:
        return float(_UNARY_OPS[type(node.op)](_eval_node(node.operand)))
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in _FUNCTIONS:
        args = [_eval_node(arg) for arg in node.args]
        return float(_FUNCTIONS[node.func.id](*args))
    raise ValueError("Unsupported expression.")
