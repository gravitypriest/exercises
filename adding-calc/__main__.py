'''
Make a calculator that lets the user add, subtract, multiply and divide
integers. It should allow exponents too. The user can only enter integers
and must expect the result to be integers. The twist is that YOU, the
programmer, can only let the program calculate expressions using addition.
Only addition. The user can enter 3*2 however you cannot calculate it using
multiplication.

Basically, the programmer is not allowed to multiply, divide and subtract
using the operations provided by a programming language. To the programmer,
the only accessible direct operation is addition.

Your calculator should be able to handle addition, subtraction, division,
multiplication and exponents. No modulo operation (to obtain the remainder
for two given operands) too.

Please note that
    -You are not allowed to use any functions (other than user-defined
    functions) to work with exponents. Basically, don't cheat by allowing
    pre-defined functions from a library for the dirty work.
    -You can use logical operators.
    -The only binary arithmetic operator that you can use is + (addition).
    -The only unary operator that you can use is ++ (increment operator).
    -No bitwise operations are allowed.
'''

import re
import sys

NEG_ONE = ''.find('a')


def _negative_check(a, b):
    negative = False
    if a < 0 or b < 0:
        negative = True
    if a < 0 and b < 0:
        negative = False
    return negative


def _flip_sign(a):
    b = 0
    while b + a != 0:
        if a < 0:
            b += 1
        else:
            b += NEG_ONE
    return b


def _abs(a):
    if a < 0:
        a = _flip_sign(a)
    return a


def add(a, b):
    return a + b


def subtract(a, b):
    c = _flip_sign(b)
    return a + c


def multiply(a, b):
    negative = _negative_check(a, b)
    a = _abs(a)
    b = _abs(b)
    count = 0
    product = 0
    while count < b:
        product += a
        count += 1
    return product if not negative else _flip_sign(product)


def divide(a, b):
    negative = _negative_check(a, b)
    a = _abs(a)
    b = _abs(b)
    if b == 0:
        return 'Cannot divide by 0'
    quotient = 0
    runner = 0
    while runner < a and (runner + b) <= a:
        runner += b
        quotient += 1
    if runner < a:
        return 'Non-integer result'
    return quotient if not negative else _flip_sign(quotient)


def exp(a, b):
    if b < 0:
        return 'Non-integer result'
    if b == 0:
        return 1
    count = 1
    product = a
    while count < b:
        product = multiply(product, a)
        count += 1
    return product


def parse_operation(input_):
    rgx = r'^(\-?\d+)\s*(\+|\-|\*|\/|\^)\s*(\-?\d+)$'
    m = re.match(rgx, input_)
    if m is None:
        print('Bad input')
        return
    a = int(m.group(1))
    op = m.group(2)
    b = int(m.group(3))
    if op == '+':
        result = add(a, b)
    if op == '-':
        result = subtract(a, b)
    if op == '*':
        result = multiply(a, b)
    if op == '/':
        result = divide(a, b)
    if op == '^':
        result = exp(a, b)
    print(result)


def main():
    while 1:
        try:
            input_ = raw_input('>> ')
            parse_operation(input_)
        except (KeyboardInterrupt, EOFError):
            print('\nBye')
            sys.exit()

if __name__ == '__main__':
    main()
