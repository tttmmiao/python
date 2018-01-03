import sys


def main():
	L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
	r = sorted(L,key=lambda L:L[0])
	for i in r:
		print(i)
if __name__ == '__main__':
	main()