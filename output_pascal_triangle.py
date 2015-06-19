import sys

def next(row):
	L = [1,]
	n = len(row)
	if n < 2:
		L.append(1)
	else:
		i,j = 0,1
		while j < n:
			a,b = row[i],row[j]
			L.append(a+b)
			i = i+1
			j = j+1
		L.append(1)
	return L
def triangles(max):
	row = [1]
	n = 1
	while n <= max:
		yield row
		row = next(row)
		n = n+1
def main():
	g = triangles(10)
	for n in g:
		print(n)
if __name__ == '__main__':
	main()