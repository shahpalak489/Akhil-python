#prime numbers
n=10
m=list(range(2,n+1))

def prime(n):
	if n>0:
		if n//2 == 1:
			print(str(n) +' is prime')	
		elif n//3 == 1:
			print(str(n) + ' is prime')
		elif n//5 == 1:
			print(str(n)+ ' is prime')

for x in m:
	prime(x)
