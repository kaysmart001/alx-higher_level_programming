#!/usr/bin/python3

if __name__ == "__main__":

	import sys

n = len(sys.argv)
arg = n - 1

if arg == 0:
	print(f"0 arguments.")

elif arg == 1:
	print(f"1 argument:")
else:
	print(f"{arg:d}: arguments:")

for i in range(1, n):
	print(f"{i:d}: {sys.argv[i]}")
