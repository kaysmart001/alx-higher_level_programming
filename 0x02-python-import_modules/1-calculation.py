#!/usr/bin/python3

if __name__ == "__main__":

	""" Program that performs some mathematical operations.

args:
a: first integer
b: second integer

return: add, sub, mul or division
"""

	from calculator_1 import add, sub, mul, div

a = 10
b = 5

print(f"{a:d} + {b:d} = {add(a, b):d}")
print(f"{a:d} - {b:d} = {sub(a, b):d}")
print(f"{a:d} * {b:d} = {mul(a, b):d}")
print(f"{a:d} / {b:d} = {div(a, b):d}")
