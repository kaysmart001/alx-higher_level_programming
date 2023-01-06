#!/usr/bin/python3

if __name__ == "__main__":

	import sys

	n = len(sys.argv)
	arg = n - 1

if arg == 0:
	print("0 arguments.")

elif arg == 1:
	print("1 argument:")
else:
	print("{:d}: arguments:".format(arg))

for i in range(1, n):
	print("{:d}: {}".format(i, sys.argv[i]))
