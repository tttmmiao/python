import sys

def is_palindrome(n):
	n_str=str(n)
	flag = True
	_len = len(n_str)
	for i in range(_len/2):
		if n_str[i]!=n_str[_len-i-1]:
			flag = False
			break
	return flag

def main():
	r=filter(is_palindrome,range(1,1000))
	for i in r:
		print(i)
if __name__ == '__main__':
	main()