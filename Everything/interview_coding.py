# sum of values
def sum(x,y):
	z=x+y
	print(z) 

#sum(10,15)

#factorial of n
n=4
fact=1
for x in range(1,n+1):
	fact=fact*x
print(fact)

#interest rate
def interest(x,y,z):
	a=(x*y*z)/100
	print(a)
#interest(100,5,5)

#armstrong number
def armstrong(a):
	b=str(a)
	c=len(b)
	x=eval(b[0])
	y=eval(b[1])
	z=eval(b[2])

	print(pow(x,c)+pow(y,c)+pow(z,c))
#armstrong(120)

#area of circle
def area(pi,r):
	redius=pi*(r*r)
	print(redius)

area(3.14,15)

