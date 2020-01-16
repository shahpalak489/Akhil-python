print("****print")
print("****print")
a=123
print (a)

print("***function")
def aki():
	print("this is not right")
aki()

def square(x):
	print(x*x)
square(2)	

def addition (x,y):
	print(x+y)
addition(3,5)

def default(x,y=5):
	print(x+y)
default(10)

default(10,y=10)

default(y=10,x=2)

def multiple(*args):
	print(args)
multiple(1,2,3,4)

print("***to call function")
print("IMP: '()' this symbol call function")
def a1():
	print("a1")
a1() # this will call function a1

print("***IMP")
def akhil():
	print("akhil")
a3=akhil() # this will call akhil function
   
def a(x):
	print(x+10)
b=a
b(2) # this will call function a

print("***to call 1 function inside another function")
def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func() #func=g  #step2: this will call function g
f(g) #step 1: this will call function f

print("***function within function")
def outside():
	def inside():
		print("i am inside") #step2
	print("i am outside") #step1
	inside() # this will call function inside
outside() # this will call function outside

print("***No call")
def inner1(): 
    print("Hello, this is before function execution") 
    func() # this will not call func unction
    print("This is after function execution")
    return inner1

print("***Return (IMP)")
def function_that_prints():
    print("I printed")

def function_that_returns():
    return "I returned"
    print("after return")

print("***The return statement terminates the execution of a function")
print("** function calling  will give only print values,not return values ")
f1 = function_that_prints() #this will call function_that_prints
f2 = function_that_returns() # this will call function_that_returns
print("***to access return values assign variable to function")
print("calling and print the variable because retuen assigns value") 
print("to function so we need to print calling function ")
print(f1)
print(f2)

print("return example 2")
def no_return(x,y):
    c = x + y
    return c
print(no_return(4,5))

print("***variables")
a="bol bhai"
print(a)

print("***variable scope")
b=100
print(b)
def scope():
	b=200
	print(b)
scope()
print(b)

print("***arithmetic Operator")
x=10
y=20
print(x+y)
print(x*y)
print(y-x)
print(y/x)

print("***comparison operator")
f=30
g=23
print(f<g)
print(f>g)
print(f==g)
print(f<=g)
print(f>=g)
print(f!=g)

print("**assignment operator**")

x += y
#Example-1
x=10
y=20
x+=y
print(x)
#example-2
x=0
for y in [1,2,3]:
	x += y
print(x)

#explanation
'''
x=0+1=1
x=1+2=3
x=3+3=6
'''

x-=y
#Example 
x=0
for y in [1,2,3]:
	x -= y
print(x)

#explanation
'''
x=0-1=-1
x=-1-2=-3
x=-3-3=-6
'''

x*=y
#Example
x=2
for y in [1,2,3]:
	x *= y
print(x)

#explanation
'''
x=2*1=2
x=2*2=4
x=4*3=12
'''

x/=y
#Example
x=4
for y in [1,2,3]:
	x /= y
print(x)

#explanation
'''
x=4/1=4
x=4/2=2
x=2/3=0.6
'''

print("**Logical operator**")
x=2
y=3
print(x>1 and y>2)
print(x==1 or y==3)
print(x==1 and y==3)

print("Membership operator")
x="california"
print('z' in x)
print('z' not in x)

x=['india','ab','ssss']
print ("ab" in x)

print("identity operator")
a=10
b=10
print(a is b)
print(a is not b)

print("Modulus")
a=10
b=3
c=2
print(a%b)  # a/b
print(a%c)  # a/c

print("*** floor division") 
print("after performing the division, give results in the lower integer to the value")
a=10
b=3
print(a//b)

print("***String operator")
print("***slice of string")
a="india"
print (a[1])

print("***slice of list")
list1=['a1','b2','c3','d4','5re']
print(list1[2])
print(list1[2:7]) 
print(list1[10:]) 
print(list1[:10])
print(list1[1:4:2])

print("***MM IMP")
#https://www.quora.com/What-is-negative-index-in-Python
print(list1[-4:-2:-1])
print("***MM IMP")
print(list1[-4:-2:1])

print("***slice With tuple")
list1=('a1','b2','c3','d4','5re')
print(list1[2])
print(list1[2:7])
print(list1[10:])
print(list1[:10])
print(list1[1:4:2])

print("***MM IMP")
print(list1[-4:-2:-1])
print("***MM IMP")
print(list1[-4:-2:1])


#slice With dics -- not possible
#slice with set -- not possible

print("***split")
print("***split with string")
a="india"
print(a.split('d'))

print("***concatenate")
b=" is a Country"
print(a+b)

print("***Repeat")
print(a*2)

print("***Replace")
c=a.replace('a','a is country')
print(c)

print("***upper case")
print(a.upper())

print("***lower case")
print(a.lower())

#change data type

print("***Conditional statement")
x=3
y=3
z=5

print("***if")
if x==3 and y==3:
	print("x and y are 3")

print("***if..else")
#case 1
if (x==z):
	print("x and z are same")
else:
	print("x and z are different")

#case 2
if True:
	print('true Condition')
else:
	print('false condition')

#case 3
if 0:
	print('true condition')
else:
	print('false condition')

#case 4
print('ratan'),print('ratan') if 10>20 else print('durga'),print('durga')

print("***if...elif...else")
if (y==z):
	print("y and z are same")
elif (x==z):
	print("x and z are different")
else:
	print("i dont know")	

print("**for Loop")
print("for loop with range")
for k in range(8):
	print(k) 
for u in range(13,19):
 	print(u)
for no in range (102,130,5):
 	print(no)

print("**for loop with List") 
fruit=["banana","apple","orange"]
for aki in fruit:
 	print(aki) 
 
print("**for ...break") #(it will stop 'for loop')
car=[2,15,19,20]
for x in car:
 	print(x)
 	if (x==15):
   		break
 
print("**for...in...continue")# ( this will not run remaining steps but will continue for loop)
for y in fruit:
	if (y=="apple"):
   	   continue
	print(y)
 
print("**for.....else**")
for z in range (5,10):
	print(z)
else:
 	print("Finally finished!")

print("**while loop**")
n = 25
while n > 20:
    print (n)
    n = n-1

print("**While...break**") #it will stop the while execution
i = 200
while i < 215:
 print(i)
 if i == 206:
   break
 i += 2

#example 2
a=1
while a<10:
	print(a)
	if a==5:
		break
	a+= 1 

print("**while...continue**") 
#it will start exceution from begining like here when i=3 its not printing i value
a=1
while a<5:
	a+= 1
	if a==3:
		continue
	print(a)

#Arrays
print("*** to convert int to string")
x=str(y)


print("** to convert List to Tuple")
List1=['a','b','c','d']
Tuple1=tuple(List1)
print(Tuple1)

print("** To convert Tuple to List")
Tuple1=('a','b','c','d')
List1=list(Tuple1)
print(List1)

print("**to convert List to set")
List1=['a','b','c','d']
set1=set(List1)
print(set1)

print("** to convert set to list")
set1={'a','b','c','d'}
List1=list(set1)
print(List1)

print("**Tuple to set")
Tuple1=('a','b','c','d')
set1=set(Tuple1)
print(set1)

print("**Tuple to Dics ")
Tuple1=('a','b','c','d')
Dict2={i:i*2 for i in Tuple1}
print(Dict2)

print("***to access Dictionary data (IMP)")
Dict3={1: 2, 2: 4, 3: 6, 4: 8, 'a': 10}
r=Dict3['a']
print(r)

r=Dict3.keys()
print(r)
r=Dict3.values()
print(r)
r=Dict3.items()
print(r)

for i in Dict3.keys():
	print(i)

for i in Dict3.values():
	print(i)

for i in Dict3.items():
	print(i)

for x,y in Dict3.items():
	print(x,'-',y)

print("exponent ")
x=10
n=2
print(x**2)
 
''' ratan '''
print('***PRINT')
eid,ename,esal=111,'ratan',100.45
print(eid)
print(ename)
print(esal)

print('Emp id=',eid)
print('Emp name=',ename)
print('Emp sal=',esal)

print('Emp id=',eid,'Emp name=',ename,'Emp sal=',esal)

print(eid,end='')  # this will print next line in same line
print(' ',ename)

print("***List of keyword")
import keyword
print(keyword.kwlist)

''' for 2.x we dont need parenthesis to print while 3.x requires parenthesis
    because we can see in 2.x print is keyword while in 3.x print is not keyword'''

print("***General Datatypes")
'''
Number : int float : 10,20   5.25, 10.29
string : str : 'ratan' "ratan"
Boolean : bool : True  False 
				   1    0
'''
evalue = 12
ename = 'ratan'
esalary = 100.92
ebool=True

print(type(evalue))
print(type(ename))
print(type(esalary))
print(type(ebool))

print('***variable')
evalue,esalary,expect=10,20,30
evalue=esalary=expect=10

print('***concatenation')
'''
we can concatenate int and float because they both are numbers
we can concatenate int and float to boolean because boolean has assigned values 0 and 1
'''
print(10+10.5)
print(10+True)
print(10+False)
print(20.5+True)

print('***not able to concatenate string and number/float/bool')
'''
print(10+'ratan')
print(10.5+'tata')
'''

print('***re assigning')
a=10
print(a)

a=100
print(a)

print('***delete')
v=10
print(v)
del v

print('***INPUT')

'''
Input takes all value as string
thats why below example will give string as result (eg:1020)

print('Example-1')
num1= input('Enter first num: ')
num2= input('Enter second num: ')
total=num1+num2
print('total:',total)


below example will give int as result

print('example-2')
num1= int(input('Enter first num: '))
num2= int(input('Enter second num: '))
total=num1+num2
print('total:',total)
'''
eid= int(input('eid: '))
ename=input('ename: ')
esal=float(input('esal: '))
print('emp id: ',eid)
print('emp name: ',ename)
print('emp salary: ',esal)


print('formatting data')

'''
int 	float		string
%d 		%g   %f 	  %s

{}

'''

# for % , if %d is first its value must be first...so its sequence is important
print('emp id =%d emp name =%s emp sal=%g' %(eid,ename,esal))


print('emp id ={} emp name ={} emp sal={}'.format(eid,ename,esal))
print('emp id ={2} emp name ={0} emp sal={1}'.format(eid,ename,esal))


print('Range')
'''
Rule: start from first value upto second value and if third value is 
	  positive move left to right and if third value is negative then
	  move right to left 
'''
for x in range(5):
	print(x)

for x in range(6,10):
	print(x)

for x in range(14,20,3):
	print(x)

for x in range(22,14,-3):
	print(x)

for x in range(-10,-1,4):
	print(x)

for x in range(-15,-27,-5):
	print(x)

