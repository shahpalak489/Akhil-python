#print
a=123
print (a)

# comment

#function
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

#variables
a="bol bhai"
print(a)

#variable scope
b=100
print(b)

def scope():
	b=200
	print(b)
scope()
print(b)

print("arithmetic Operator")
x=10
y=20
print(x+y)
print(x*y)
print(y-x)
print(y/x)

print("comparison operator")
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

print("String operator")
print("slice with string")
a="india"
print (a[1])

print("slice with list")
list1=['a1','b2','c3','d4','5re']
print(list1[2])
print(list1[2:7])
print(list1[10:])
print(list1[:10])

print("slice With tuple")
list1=('a1','b2','c3','d4','5re')
print(list1[2])
print(list1[2:7])
print(list1[10:])
print(list1[:10])

#slice With dics -- not possible
#slice with set -- not possible

print("split")
print("split with string")
a="india"
print(a.split('d'))

print("concatenate")
b=" Is Country"
print(a+b)

print("Repeat")
print(a*2)

print("Reverse string")
print(a[::-1])

print("Replace")
c=a.replace('a','a is country')
print(c)

print("upper case")
print(a.upper())

print("lower case")
print(a.lower())

#change data type

print("Conditional statement")
x=3
y=3
z=5

print("if")
if (x==y):
	print("x and y are same")

print("if..else")
if (x==z):
	print("x and z are same")
else:
	print("x and z are different")

print("if...elif...else")
if (y==z):
	print("y and z are same")
elif (x==z):
	print("x and z are different")
else:
	print("i dont know")	

#switch statement


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
 
print("**for ...break") #( it will stop for loop)
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
for no in range (5,10):
 print(no)
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


print("**Comprehensions**")
print("**List Comprehensions**")
List1=(1,2,3,4,5)
x=[i for i in List1]
# same as for i in List1:
#             if....
#			print(i)
print(x)

x=[i*2 for i in List1]
print(x)

x=[i*2 for i in List1 if i==4]
print(x)

x=[i*3 for i in List1 if (i*3)<12]
print(x)

print("**Set comprehension**")
List1=[1,2,3,4,5]
x={i for i in List1}
print(x)

x={i*2 for i in List1}
print(x)

print("**see**")
x={i*2 for i in list1 if i==4}
print(x)

x={i*3 for i in List1 if (i*3)<12}
print(x)

print("**Dict  Comprehensions**")
List1={1,2,3,4,5}
x={i:i for i in List1}
print(x)

x={i:i*2 for i in List1}
print(x)

x={i:i*2 for i in List1 if i==4}
print(x)

x={i:i*3 for i in List1 if (i*3)<12}
print(x)

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

print("**Tuple to Dics")
Tuple1=('a','b','c','d')



print("**Lambda")
print("** Lambda with given function name")
akhil=lambda a: a+6
# same as def akhil(x)
#			  x+6
print(akhil(10))

akhil=lambda a,b: a+b
print(akhil(2,5))

akhil=lambda a,b,c: a+(2*b)+(3*c)
print(akhil(2,3,5))

print("**Lambda as anonymus(function name not given)")
print("see-how a value is 1?")
#example 1
def myfunc(n):
  return lambda a : a-n
mytripler = myfunc(15)
print(mytripler(1))

#example 2
def testfunc(num):
    return lambda x : x * num
result1 = testfunc(10)
print(result1(9))

print("**see  - Lambda as anonymus with filter**")
numbers_list = [2, 6, 8, 11, 4, 12, 7, 13, 17, 0, 3, 21,10]
filtered_list = list(filter(lambda num: (num > 7), numbers_list))
print(filtered_list)

print("**see   - Lambda as anonymus with map**")
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
mapped_list = list(map(lambda num: num % 2, numbers_list))
print(mapped_list)







print("**Generators")



print("**Decorator**")





