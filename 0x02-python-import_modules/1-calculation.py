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

	print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
	print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
	print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
	print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
