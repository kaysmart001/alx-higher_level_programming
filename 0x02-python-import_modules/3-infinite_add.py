#!/usr/bin/python3

if __name__ == "__main__":

	import sys

n = len(sys.argv)
#arg = n - 1

#if arg == 0:
#	print(f"0")
#else:
for i in range(1, n):
	total = 0
	total = total + int(sys.argv[i])
	print(f"{total:d}")

